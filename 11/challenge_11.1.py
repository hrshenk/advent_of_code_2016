from collections import deque
from itertools import *

class state():
    def __init__(self):
        self.floors = [ [None], [None], [None], [None] ]
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
        hypothetical = (self.floors[floor] + [item1, item2])
        return self.is_valid_floor(hypothetical)
            
    def is_valid_floor(self, floor):
        floor = floor.remove(None)
        if floor == None:
            return True
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
                    print key
                    return False
        return True
        
    #breadth first search to find shortest path
    def find_path(self, target_node):
        current_q = deque()
        current_q.appendleft(self)
        next_q = deque()
        seen = {}
        target_config = (target_node.elevator, target_node.floors)
        seen[frozenset(self.floors)] = True
        
        while current_q:
            node = current_q.pop()
            elevator = node.elevator
            floors = node.floors
            combos = combinations( node.floors[elevator], 2 )
            for item1, item2 in combos:
                node.is_valid_move(item1, item2, elevator + 1)

#input.  items are in form (color, type)
floor1 = [ None, ("promethium", "gen"), ("promethium", "chip") ]
floor2 = [ None, ("cobalt", "gen"), ("curium", "gen"), ("ruthenium", "gen"), ("plutonium", "gen")]
floor3 = [ None, ("cobalt", "chip"), ("curium", "chip"), ("ruthenium", "chip"), ("plutonium", "chip")]
floor4 = [ None ]

start_node = state()
start_node.floors = [ floor1, floor2, floor3, floor4 ]

current_q = deque()
next_q = deque()
test_node = state()
test_node.floors = [ floor1, floor2, floor3, floor4 ]
print start_node.find_path(test_node)
