import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib import cm
import numpy as np

import sys
sys.path.insert(0,'../npcirclepack') #import from local directory
import npcirclepack

CMAP = cm.get_cmap('viridis', 8)

def get_color(i, max_depth):
    return CMAP(i/max_depth)

def recursively_add_circles(ax, x, y, r, node, depth, max_depth):
    circle = plt.Circle((x, y), r, color=get_color(depth, max_depth))
    ax.add_artist(circle)
    if 'children' in node:
        for i in range(len(node['children'])):
            recursively_add_circles(ax, node['pos'][i,0], node['pos'][i,1], node['pos'][i,2], node['children'][i], depth+1, max_depth)

def calc_max_depth(node, depth):
    if 'children' in node and len(node['children'])>0:
        print(node['children'])
        return max([calc_max_depth(node['children'][i], depth+1) for i in range(len(node['children']))])
    else:
        return depth+1


def show_result(root):
    fig, ax = plt.subplots(1)
    ax.set_aspect(1)
    plt.xlim(-1.05,1.05)
    plt.ylim(-1.05,1.05)
    plt.title("Circle Packing Example")
    max_depth = calc_max_depth(root, 0)
    recursively_add_circles(ax, 0, 0, root['r'], root, 0, max_depth)
    plt.show()

def create_hierarchy():
    root = {
        'children': [
            {'children': [{'r':3},{'r':5},{'r':1}]},
            {'r': 2},
            {'r': 3},
        ]
    }
    return root

def main():
    root = create_hierarchy()
    # breakpoint()
    npcirclepack.pack_enclose_hierarchy(root, padding=0.5)
    # breakpoint()
    show_result(root)

if __name__=="__main__":
    main()