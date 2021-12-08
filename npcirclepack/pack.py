import numpy as np

from npcirclepack.enclose import encloseFrontChain
from npcirclepack.node import Node

def place(pos, b, a, c):
    #distance squared between a and b
    dx = b.x-a.x
    dy = b.y-a.y
    d2 = dx*dx + dy*dy

    if (d2):
        #desired distance sq between a, c
        a2 = a.r + pos[c][2]
        a2 *= a2
        #desired distance sq between b, c
        b2 = b.r + pos[c][2]
        b2 *= b2

        if (a2 > b2): #or, if a.r > b.r
            x = (d2 + b2 - a2) / (2 * d2)
            y = np.sqrt(max(0, b2 / d2 - x * x))
            #place circle c 
            pos[c][0] = b.x - x*dx - y*dy
            pos[c][1] = b.y - x*dy + y*dx
        else:
            x = (d2 + a2 - b2) / (2 * d2)
            y = np.sqrt(max(0, a2 / d2 - x * x))
            pos[c][0] = a.x + x*dx - y*dy
            pos[c][1] = a.y + x*dy + y*dx
    else:
        #if b and a are the same point just put c somewhere sensible
        pos[c][0] = a.x + a.r + pos[c][2]
        pos[c][1] = a.y

def intersects(a, b):
    dr = a.r + b.r - 1e-3
    dx = b.x - a.x
    dy = b.y - a.y
    return dr*dr > dx*dx + dy*dy

def score(a):
    b = a.next
    ab = a.r + b.r
    #weighted position (weighed based on rad)
    dx = (a.x * b.r + b.x * a.r) / ab
    dy = (a.y * b.r + b.y * a.r) / ab
    #distance squared from origin to weighted center
    return dx*dx + dy*dy        

def pack_enclose(pos):
    #place the first circle
    pos[0][0] = 0 #x0=0
    pos[0][1] = 0 #y0=0
    if len(pos)==1:
        #done, and enclosing circle is just the circle
        return pos[0][2]
    
    #place second circle
    pos[0][0] = -pos[1][2] #x0=-r1
    pos[1][0] = pos[0][2] #x1=r0
    pos[1][1] = 0 #y1=0
    if len(pos)==2:
        #done, and enclosing circle has radius of sum of the 2 radii
        return pos[0][2]+pos[1][2]
    
    #place third circle
    a = Node.from_np(0, pos)
    b = Node.from_np(1, pos)
    place(pos, b, a, 2) #b is second circle, a is first, c is third

    #initialize front-chain using the first 3 circles
    c = Node.from_np(2, pos)
    a.next = b
    a.prev = c
    b.next = c
    b.prev = a
    c.next = a
    c.prev = b

    #place each circle in turn
    for i in range(3, len(pos)):
        count = 0
        while True:
            count += 1
            if count>2*len(pos):
                print("Definite infinite loop! Exiting")
                exit(-1)
            #attempt to place
            place(pos, a, b, i)
            c = Node.from_np(i, pos)

            #check if where we added c intersects any circles in the front-chain
            j = b.next
            k = a.prev
            sj = j.r
            sk = k.r
            try_again=False
            while True:
                if sj <= sk:
                    if intersects(j, c):
                        try_again=True
                        b = j
                        a.next = b
                        b.prev = a
                        break
                    sj += j.r
                    j = j.next
                else:
                    if intersects(k, c):
                        try_again=True
                        a = k
                        a.next = b
                        b.prev = a
                        break
                    sk += k.r
                    k = k.prev

                if j==k.next: #we've checked all the circles in the front-chain
                    break
            if try_again:
                continue

            #success!
            c.prev = a
            c.next = b
            a.next = c
            b.prev = c
            b = c

            #compute new closest circle pair to centroid
            aa = score(a)
            while c != b:
                ca = score(c)
                if ca<aa:
                    a = c
                    aa = ca
                c = c.next
            b = a.next
            break

    #done packing!

    #find enclosing circle
    #get indices of front-chain circles
    nodes = [b]
    c = b.next
    while c!=b:
        nodes.append(c)
        c = c.next
    
    e = encloseFrontChain(nodes)
    pos[:,:2] -= np.array([e.x, e.y]) #translate to put enclosing circle about origin
    return e.r