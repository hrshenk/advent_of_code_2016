from itertools import *
from collections import deque

def test_parity(x, y, favorite):
    num = (x*x + 3*x + 2*x*y + y + y*y) + favorite
    bits = bit_count(num)
    return bits % 2
    
    
def bit_count(num):
    count = 0
    while num:
        if num & 1:
            count += 1
        num = num >> 1
    return count
    
#define our input
favorite = 1350
target = (31, 39)
#favorite = 10
#target = (7, 4)
current = deque()
frontier = deque()
seen = {}
level = 0
current.appendleft( (1, 1) )
seen[(1, 1)] = None 
while current:
    x, y = current.pop()
    edges = []
    for i in [-1, 1]:
        if x + i >= 0:
            edges.append( (x+i, y) )
        if y + i >= 0:
            edges.append( (x, y+i) )
    for u, v in edges:
        if (u, v) == target:
            print level + 1
            quit()
        if not test_parity(u, v, favorite):
            if not seen.has_key( (u, v) ):
                frontier.appendleft( (u, v) )
                seen[(u, v)] = (x, y)
    if not current:
        level += 1
        if level == 50:
            print len(seen)
            quit()
        current = frontier
        frontier = deque()