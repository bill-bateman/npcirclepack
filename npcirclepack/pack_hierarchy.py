import numpy as np

from npcirclepack.pack import pack_enclose

def scale_node(node, k, parent_coords):
    scale_node_inner(node, k, parent_coords)
    if 'children' in node:
        for i in range(len(node['children'])):
            scale_node(node['children'][i], k, node['pos'][i,:2])

def scale_node_inner(node, k, parent_coords):
    if 'pos' in node:
        node['pos'][:,:] *= k #multiply all by scaling factor (to fit in 2x2 box)
        node['pos'][:,:2] += parent_coords #center around parent
        #during pack_enclose function, we always assume parent will be centered at (0,0)
        #so we just add the parent's actual location now

def pack_children_inner(node, padding):
    if 'children' not in node or len(node['children'])==0:
        return
    node['pos'] = np.zeros((len(node['children']),3), dtype=np.float32)
    for i in range(len(node['children'])):
        if 'r' in node['children'][i]:
            node['pos'][i][2] = node['children'][i]['r'] + padding
    
    node['r'] = pack_enclose(node['pos']) + padding
    node['pos'][:,2] -= padding

def pack_children(node, padding):
    #post order traversal
    if 'children' in node:
        for n in node['children']:
            pack_children(n, padding)
    pack_children_inner(node, padding)

def layout_circle_pack(hierarchy, padding): 
    pack_children(hierarchy, padding) #post-order traversal to pack all nodes

    #now scale to fit within a 2x2 box
    k = 1 / hierarchy['r'] #technically it's min(w,h) / (2*r) but for us that simplifies to 1/r
    hierarchy['r'] = 1 #r*k = r/r = 1
    scale_node(hierarchy, k, np.zeros(2, dtype=np.float32)) #pre-order traversal to scale nodes