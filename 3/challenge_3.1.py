file = open('input.txt', 'r')
count = 0

for line in file:
    x,y,z = sorted( map( int, line.split() ) )
    if x + y > z:
        count += 1
print count
