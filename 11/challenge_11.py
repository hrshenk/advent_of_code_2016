from collections import deque
from itertools import *
import copy

class state():
    def __init__(self):
        self.floors = [ {None}, {None}, {None}, {None} ]
        self.elevator = 0
        
    def is_valid_move(self, item1, item2, floor):
        if floor < 0 or 3 < floor:
            return False
        #must have one cargo item
        if item1 == None and item2 == None:  
            return False
        #we can only move up or down
        if abs(floor - self.elevator) != 1:
            return False
        #if the types are different then they must be the same color
        if ( item1 != None and item2 != None ) and ( item1[1] != item2[1] ) and ( item1[0] != item2[0] ):
            return False
        hypothetical1 = self.floors[floor] | ({item1, item2})
        hypothetical2 = self.floors[self.elevator] - ({item1, item2})
        return self.is_valid_floor(hypothetical1) and self.is_valid_floor(hypothetical2)
            
    def is_valid_floor(self, floor):
        floor = floor.difference({None})
        gens = {}
        chips = {}
        for item in floor:
            if item[1] == "gen":
                gens[item[0]] = True
            else:
                chips[item[0]] = True
        if gens == {} or chips == {}:
            return True
        else:
            for key, value in chips.items():
                if not gens.has_key(key):
                    return False
        return True
        
    #breadth first search to find shortest path
    def find_path(self, target_node):
        current_q = deque()
        current_q.appendleft(self)
        next_q = deque()
        seen = {}
        target_config = target_node.floors
        level = 0
        while current_q:
            node = current_q.pop()
            combos = combinations( node.floors[node.elevator], 2 )
            for item1, item2 in combos:
                #for each pair try moving up and try moving down
                for i in [-1, 1]:
                    #if we have a valid move, then we'll make the move and add that node to the queue for exploration
                    if node.is_valid_move(item1, item2, node.elevator + i):
                        new_node = copy.deepcopy(node)
                        new_node.elevator += i
                        new_node.floors[ new_node.elevator - i ] -= ( {item1, item2} - {None} )
                        new_node.floors[ new_node.elevator ] |= {item1, item2}
                        if new_node.floors == target_config:
                            print "winner chkin drinner"
                            print level
                            return True
                        if not seen.has_key( tuple( map(frozenset,new_node.floors) + [new_node.elevator] ) ):
                            next_q.appendleft(new_node)
            seen[tuple( map(frozenset, node.floors) + [node.elevator] )] = True
            if len(current_q) == 0 and len(next_q) != 0:
                current_q = next_q
                next_q = deque()
                level += 1
                print level
                
#floor4 = { None }
#floor3 = { None, ("cobalt", "chip"), ("curium", "chip"), ("ruthenium", "chip"), ("plutonium", "chip")}
#floor2 = { None, ("cobalt", "gen"), ("curium", "gen"), ("ruthenium", "gen"), ("plutonium", "gen")}
#floor1 = { None, ("promethium", "gen"), ("promethium", "chip") }

floor4 = { None }
floor3 = { None, ("L", "gen")}
floor2 = { None, ("H", "gen")}
floor1 = { None, ("H", "chip"), ("L", "chip") }

start_node = state()
start_node.floors = [ floor1, floor2, floor3, floor4 ]
target_floor = {None}
for floor in start_node.floors:
    target_floor.update(floor)
test_node = state()
test_node.floors = [ {None}, {None}, {None}, target_floor ]
print start_node.find_path(test_node)