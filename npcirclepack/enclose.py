import math
import random

from npcirclepack.node import Node

def extend(arr, p):
    #find the set of circles (1, 2, or 3) whose enclosure encloses all the circles in arr and p

    if enclosesWeakAll(p, arr):
        #p encloses all of arr
        return [p]
    
    #if we get here then arr must have at least one element
    for i in range(len(arr)):
        #check if any one circle in arr, when combined with p, can enclose all of arr
        if enclosesNot(p, arr[i]) and enclosesWeakAll(enclose2(arr[i], p), arr):
            return [arr[i], p]
    
    #if we get here then arr must have at least 2 elements
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            #check if any 2 circles in arr, when combined with p, can enclose all of arr
            if enclosesNot(enclose2(arr[i], arr[j]), p) \
                and enclosesNot(enclose2(arr[i], p), arr[j]) \
                and enclosesNot(enclose2(arr[j], p), arr[i]) \
                and enclosesWeakAll(enclose3(arr[i], arr[j], p), arr):
                    return [arr[i], arr[j], p]
    
    #we shouldn't get here
    raise Exception("Error in npcirclepack.enclose. This should not happen!")

def enclosesNot(a, b):
    dr = a.r - b.r
    dx = b.x - a.x
    dy = b.y - a.y
    return (dr < 0) or (dr*dr < (dx*dx + dy*dy))

def enclosesWeak(a, b):
    dr = a.r - b.r + max(a.r, b.r, 1) * 1e-5 #fudge factor
    dx = b.x - a.x
    dy = b.y - a.y
    return (dr > 0) and (dr*dr > (dx*dx + dy*dy))

def enclosesWeakAll(e, arr):
    for i in range(len(arr)):
        if not enclosesWeak(e, arr[i]):
            return False
    return True

def enclose(arr):
    if len(arr)==1:
        return enclose1(arr[0])
    if len(arr)==2:
        return enclose2(arr[0], arr[1])
    if len(arr)==3:
        return enclose3(arr[0], arr[1], arr[2])

def enclose1(a):
    return a

def enclose2(a, b):
    #enclose 2 circles
    x1 = a.x
    y1 = a.y
    r1 = a.r
    
    x2 = b.x
    y2 = b.y
    r2 = b.r

    x21 = x2 - x1
    y21 = y2 - y1
    r21 = r2 - r1

    l = math.sqrt(x21 * x21 + y21 * y21)
    
    x = (x1 + x2 + x21 / l * r21) / 2
    y = (y1 + y2 + y21 / l * r21) / 2
    r = (l + r1 + r2) / 2
    return Node(x, y, r)

def enclose3(a, b, c):
    #enclose 3 circles
    x1 = a.x
    y1 = a.y
    r1 = a.r

    x2 = b.x
    y2 = b.y
    r2 = b.r

    x3 = c.x
    y3 = c.y
    r3 = c.r

    a2 = x1 - x2
    a3 = x1 - x3

    b2 = y1 - y2
    b3 = y1 - y3

    c2 = r2 - r1
    c3 = r3 - r1

    d1 = x1 * x1 + y1 * y1 - r1 * r1
    d2 = d1 - x2 * x2 - y2 * y2 + r2 * r2
    d3 = d1 - x3 * x3 - y3 * y3 + r3 * r3

    ab = a3 * b2 - a2 * b3
    xa = (b2 * d3 - b3 * d2) / (ab * 2) - x1
    xb = (b3 * c2 - b2 * c3) / ab
    ya = (a3 * d2 - a2 * d3) / (ab * 2) - y1
    yb = (a2 * c3 - a3 * c2) / ab

    aa = xb * xb + yb * yb - 1
    bb = 2 * (r1 + xa * xb + ya * yb)
    cc = xa * xa + ya * ya - r1 * r1

    r = ((bb + math.sqrt(bb * bb - 4 * aa * cc)) / (2 * aa)) if aa!=0 else cc/bb
    r *= -1

    x = x1 + xa + xb*r
    y = y1 + ya + yb*r
    return Node(x, y, r)

def encloseFrontChain(nodes):
    #shuffling makes it faster
    random.shuffle(nodes)

    arr = []
    e = None
    i=0
    while True:
        if i>=len(nodes):
            break
    
        if e!=None and enclosesWeak(e, nodes[i]):
            i+=1
            continue
        else:
            arr = extend(arr, nodes[i])
            e = enclose(arr)
            i=0
            continue
    
    return e
        
        


