from itertools import *
from heapq import *

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


def taxicab_distance(point1, point2):
    d = 0
    for x, y in zip(point1, point2):
        d += abs(x - y)
    return d
        
        
#define our input
favorite = 1350
#favorite = 10
#target = (7, 4)
target = (31, 39)
start = (1, 1)
heap = []  #this will be our priority queue
seen = {}
cost = 0
#our heap will be prioritize by estimated cost to arrive at target
#and will contain tuples of the form 
#(estimated cost, current cost to arrive at node, node coordinates)
heappush(heap, ( taxicab_distance(start, target), 0, start))
while heap:
    item = heappop(heap)
    cost = item[1] + 1 #this is the cost of arriving at neighbors via the current path
    x, y = item[2]
    seen[(x, y)] = True
    #edges will contain nodes adjacent to the current node
    edges = []
    for i in [-1, 1]:
        if x + i >= 0:
            edges.append( (x+i, y) )
        if y + i >= 0:
            edges.append( (x, y+i) )
    for u, v in edges:
        if (u, v) == target:
            print cost
            quit()
        if not test_parity(u, v, favorite):
            if not seen.has_key( (u, v) ):
                heappush( heap, (cost + taxicab_distance((x,y), target), cost, (u, v)) )
    seen[(x, y)] = True

        


    
    