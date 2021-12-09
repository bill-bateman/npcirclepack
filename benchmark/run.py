import timeit
import numpy as np
import random

import sys
sys.path.insert(0,'../npcirclepack') #import from local directory
import npcirclepack

def rand_radius():
    return random.random()*20

def test(pos):
    npcirclepack.pack_enclose(pos)

def main():
    length = 1000
    if len(sys.argv)==2:
        length = int(sys.argv[1])
    pos = np.zeros((length,3), dtype=np.float32)
    for i in range(length):
        pos[i,2]=rand_radius()
    
    result = timeit.timeit(lambda: test(pos), number=1)
    print(f"Circle packing {length} circles took {result} seconds.")

if __name__=="__main__":
    main()