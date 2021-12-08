import numpy as np
import pack

def pack_enclose(pos):
    #pos should be either a 1D numpy array of radii
    #or a 2D numpy array with a second dimension of length 3
    #first 2 values will be x,y (will be clobbered). 3rd value is r (not clobbered)

    #handle input
    if len(pos.shape)==1:
        #can take 1D array of radii
        rs = pos
        pos_dtype = rs.dtype
        if pos_dtype!=np.float32 and pos_dtype!=np.float64:
            pos_dtype=np.float32
        pos = np.zeros((len(rs), 3),dtype=rs.dtype)
        pos[:,2]=rs #copy radii into pos array
    return pack.pack_enclose(pos)
    