import numpy as np
from npcirclepack import pack, pack_hierarchy

def pack_enclose(pos):
    """Performs circle packing in-place in the given numpy array.
    
    Note that for the passed array, the 2 values will be x and y (will be clobbered). 3rd value is the input radius (not clobbered).

    Parameters
    ----------
    pos : ndarray
        2D numpy array with second dimension of length 3

    Returns
    -------
    float
        Radius of enclosing circle. The center of the enclosing circle is assumed to be (0,0).

    """
    if len(pos.shape)!=2:
        raise Exception("Expected a 2D numpy array.")
    if pos.shape[1]!=3:
        raise Exception("Expected a 2D numpy array with a second dimension of 3.")
    if pos.dtype!=np.float32 and pos.dtype!=np.float64:
        raise Exception("Expected a 2D numpy array with data type of float32 or float64.")
    return pack.pack_enclose(pos)
    
def pack_enclose_hierarchy(hierarchy, padding=0):
    """Performs circle packing on the provided hierarchy.
    
    For each node with children, this function will set:
    - `r` to the radius of that node (sucth that it encloses its children)
    - `pos` to a numpy array containing the float32 values for x, y, r of its children.
    
    Note that the function scales the circles such that the final enclosing circle has a radius of 1.
    i.e. to fit within a 2x2 viewing pane (x and y are [-1,1]).
    
    Each node within the passed hierarchy should have the following fields:
        - children: array of nodes
        - r: int/float (only needs to be set for leaf nodes)

    Parameters
    ----------
    hierarchy : dict
        Hierarchy should be a dictionary representing the root object of a hierarchy to lay out.
    padding : float
        How much spacing to put between each circle (default 0).

    Returns
    -------

    """
    pack_hierarchy.layout_circle_pack(hierarchy, padding)