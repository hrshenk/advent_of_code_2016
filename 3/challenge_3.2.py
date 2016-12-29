import numpy as np
file = open("input.txt", 'r')
m = []
count = 0
i=0
j=0

for line in file:
    m.append( map( int, line.split() ) )
    if i%3 == 2:
        m = np.transpose(m)
        for j in xrange(3):
            x, y, z = sorted(m[j])
            if x + y > z:
                count += 1
        m = []
    i+=1
print count