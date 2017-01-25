from collections import deque
from itertools import *
import copy

class State():
    def __init__(self):
        self.elevator = None
        self.floors = None
        self.config = None
        self.low_floor = None
    
    def set_low_floor(self):
        for i, c in enumerate(self.config):
            if c["g"] != 0 or c["m"] != 0:
                self.low_floor = i
                return i
                
    def is_valid_move(self, step, item1 = None, item2 = None): 
        #we only move one floor at a time
        new_elev = self.elevator + step
        if abs(step) != 1: return False
        #lets not go too low
        if new_elev < self.low_floor: return False
        #lets not go too high
        if new_elev  > 3: return False
        #lets not wander too far from the lowest floor
        if new_elev - self.low_floor > 2: return False
        #case move 2 items
        if item1 and item2:
            #case generator and microchip
            if item1[0] != item2[0]:
                #lets make sure we don't damage any chips with our move
                if self.config[new_elev]["g"] < self.config[new_elev]["m"]:
                    return False
            #case two chips
            elif item1[0] == "m":
                #case two microchips
                #ensure we don't move to a floor with generators
                #unless both corresponding generators are there to protect us
                if self.config[new_elev]["g"] != 0:
                    for item in [item1, item2]:
                        if item[2] != new_elev:
                            return False
            #case two generators
            else:
                #lets not leave behind any vulnerable chips
                if self.config[self.elevator]["g"] > 2:
                    if item1[2] == self.elevator or item2[2] == self.elevator:
                        return False
                #lets not compromise any unprotected chips on the new_elev floor
                #if there are already generators on that floor, then all chips should already be protected
                #otherwise...
                if self.config[new_elev]["g"] == 0:
                    chip_count = self.config[new_elev]["m"]
                    for item in [item1, item2]:
                        if item[2] == new_elev: chip_count -= 1
                    if chip_count > 0:
                        return False
            
        #case moving only one item
        else:
            item = item1 if item1 else item2
            if not item:
                return False
            #case single generator.
            if item[0] == "g":
                chip_count = self.config[new_elev]["m"] - self.config[new_elev]["g"]
                #too many unprotected chips on new_elev floor
                if chip_count > 1:
                    return False
                #only one unprotected chip on new_elev floor.  Does it correspond to the gen we're trying to move?
                elif chip_count == 1 and item[2] != new_elev:
                    return False
                #lets make sure we aren't leaving behind an unprotected chip
                if self.config[self.elevator]['g'] > 1:
                    if item[2] == self.elevator:
                        return False
            #case single chip
            else:
                #if there are generators on new_elev floor we must make sure our chip is protected
                if self.config[new_elev]['g'] != 0:
                    if item[2] != new_elev:
                        return False
        return True
    
    def move_items(self, step, item1 = None, item2 = None):
        new_elev = self.elevator + step
        assert ( 0 <= new_elev and new_elev <= 3 )
        items = [ item for item in [item1, item2] if item ]
        same_color = False
        if item1 and item2:
            same_color = item1[1] == item2[1]
        for item in items:
            #remove item from current floor
            self.floors[self.elevator].discard(item)
            #update config counts
            self.config[self.elevator][item[0]] -= 1
            self.config[new_elev][item[0]] += 1
            #update the compliment items and add item to new floor
            if same_color:
                item = list(item)
                item[2] = new_elev
                self.floors[new_elev].add(tuple(item))
                
            elif item[0] == "m":
                self.floors[new_elev].add(tuple(item))
                compliment = ["g", item[1], self.elevator]
                self.floors[item[2]].discard(tuple(compliment))
                compliment[2] = new_elev
                self.floors[item[2]].add(tuple(compliment))
                
            else:
                self.floors[new_elev].add(tuple(item))
                compliment = ["m", item[1], self.elevator]
                self.floors[item[2]].discard(tuple(compliment))
                compliment[2] = new_elev
                self.floors[item[2]].add(tuple(compliment))
        self.set_low_floor()
        self.elevator = new_elev

#-----------------------------body----------------------------#
#define our input
floor4 = set([])
floor3 = { ("m", "cobalt", 1), ("m", "curium", 1 ), ("m", "ruthenium", 1), ("m", "plutonium", 1) }
floor2 = { ("g", "cobalt", 2), ("g", "curium", 2 ), ("g", "ruthenium", 2), ("g", "plutonium", 2) }
floor1 = { ("g","promethium", 0), ("m","promethium", 0), ("g", "elerium", 0), ("m", "elerium", 0), ("g", "dilithium", 0), ("m", "dilithium", 0) }
counts = [ {"g":3, "m":3}, {"g":4, "m":0}, {"g":0, "m":4}, {"g":0, "m":0} ]


#Input for Part 1
#floor4 = set([])
#floor3 = { ("m", "cobalt", 1), ("m", "curium", 1 ), ("m", "ruthenium", 1), ("m", "plutonium", 1) }
#floor2 = { ("g", "cobalt", 2), ("g", "curium", 2 ), ("g", "ruthenium", 2), ("g", "plutonium", 2) }
#floor1 = { ("g","promethium", 0), ("m","promethium", 0) }
#counts = [ {"g":1, "m":1}, {"g":4, "m":0}, {"g":0, "m":4}, {"g":0, "m":0} ]

#initialize the first node
start_node = State()
start_node.elevator = 0
start_node.floors = [ floor1, floor2, floor3, floor4 ]
start_node.config = counts
start_node.set_low_floor()
#define our queues for breadth first search
current = deque() 
frontier = deque()
seen = {}
current.appendleft(start_node)
level = 0
while current:
    node = current.pop()
    elevator = node.elevator
    floor = node.floors[elevator]
    #valid move of two items include only ones where color or type are equal
    c = [ x for x in combinations(floor, 2) if x[0][0] == x[1][0] or x[0][1] == x[1][1] ]
    h = {}
    d = []
    #we'll prune moves that don't make sense
    for a, b in c:
        t = frozenset( [( a[0], a[2] ), ( b[0], b[2] ) ] )
        if not h.has_key(t):
            d.append( (a, b) )
            h[t] = True
    for a in floor:
        t = ( a[0], a[2] )
        if not h.has_key(t):
            d.append( (a, None) )
            h[t] = True
    #each potential move in d should now give rise to a potentially interesting configuration
    #since we've pruned redundant moves
    for i in [-1, 1]:    
        for item1, item2 in d:
            if node.is_valid_move(i, item1, item2):
                new = copy.deepcopy(node)
                new.move_items(i, item1, item2)
                if new.low_floor == 3:
                    print "Wirner chikin dirner"
                    print level + 1
                    quit()
                key = [ tuple([x["g"], x["m"]]) for x in new.config ]
                key.append(new.elevator)
                key = tuple(key)
                if not seen.has_key(key):
                    frontier.appendleft(new)
    key = [ tuple([x["g"], x["m"]]) for x in node.config ]
    key.append(node.elevator)
    key = tuple(key)
    seen[key] = True
    if not current:
        current = frontier
        frontier = deque()
        print "level", level
        print len(current)
        level += 1

        
    
    
        
    
    
    
        
    
    


