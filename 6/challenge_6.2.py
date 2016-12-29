file = open("input.txt", 'r')
m = []
column = []
for line in file:
    m.append(line)

#minus 1 because we care not about \n
for i in xrange( len(m[0])-1 ): 
    column.append({})
    for j in xrange(len(m)):
        if column[i].has_key(m[j][i]):
            column[i][ m[j][i] ] += 1
        else:
            column[i][ m[j][i] ] = 1
for h in column:
    print min(h, key=h.get)
