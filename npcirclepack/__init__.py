import numpy as np
from npcirclepack import pack

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
    