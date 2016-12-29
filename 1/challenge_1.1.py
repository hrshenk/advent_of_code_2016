file = open('input.txt', 'r')
directions = file.read().split(', ')
direction = 0 # 0 is North, 1 is East, 2 is South, 3 is West
coordinates = [0, 0, 0, 0]
for d in directions:
    #determine how many blocks we'll travel in this instruction
    blocks = int(d[1:])
    #determine the direction we'll be facing
    if d[0] == 'L':
        direction = (direction - 1) % 4
        coordinates[direction] += blocks
    elif d[0] == 'R':
        direction = (direction + 1) % 4
        coordinates[direction] += blocks
print coordinates
coordinates[0] = coordinates[0] - coordinates[2]
coordinates[1] = coordinates[1] - coordinates[3]


print abs( coordinates[0] ) + abs( coordinates[1] )


        
    