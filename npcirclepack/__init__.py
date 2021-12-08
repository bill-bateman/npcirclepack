import numpy as np
from npcirclepack import pack, pack_hierarchy

def pack_enclose(pos):
    #pos should be a 2D numpy array with a second dimension of length 3
    #first 2 values will be x,y (will be clobbered). 3rd value is r (not clobbered)
    if len(pos.shape)!=2:
        raise Exception("Expected a 2D numpy array.")
    if pos.shape[1]!=3:
        raise Exception("Expected a 2D numpy array with a second dimension of 3.")
    if pos.dtype!=np.float32 and pos.dtype!=np.float64:
        raise Exception("Expected a 2D numpy array with data type of float32 or float64.")
    return pack.pack_enclose(pos)
    
def pack_enclose_hierarchy(hierarchy, padding=0):
    #hierarchy should be a dictionary representing the root object of a hierarchy to layout.
    #each node should have the following fields:
    # - children: [nodes]
    # - r: Number (should only be set for leaf nodes)
    #
    #this function will, for each node with children, set
    # - r to the radius of that node (such that it encloses its children)
    # - pos to a numpy array containing the float32 x, y, r values of its children
    #
    #Note that the function scales the radii such that the final enclosing circle has a radius of 1.
    #i.e. to fit within a 1x1 viewing pane.
    pack_hierarchy.layout_circle_pack(hierarchy, padding)