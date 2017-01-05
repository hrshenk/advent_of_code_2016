import re

def get_ABA(string):
    h = {}
    for i in xrange( len(string)-2 ):
        if ( string[i] != string[i+1] ) and ( string[i] == string[i+2] ) :
            h[ (string[i] + string[i+1] ) ] = 1
    return h

def test_BAB(string, h_table):
    for i in xrange( len(string) - 2 ) :
        if ( string[i] != string[i+1] ) and ( string[i] == string[i+2] ) :
                if h_table.has_key( ( string[i+1] + string[i] ) ):
                    return True
    return False
    
file = open("input.txt", 'r')
count = 0
for line in file:
    flag = False
    line = line.strip("\n")
    m = re.split("[\[\]]", line)
    #due to structure of input, odd rows of m are 'hypernet' sequences
    #even rows are supernet sequences
    for i in xrange( len(m)/2 + 1 ):
        aba = get_ABA(m[2*i])
        if aba != {}:
            for j in xrange( len(m)/2 ):
                if test_BAB(string = m[2*j + 1], h_table = aba):
                    count += 1
                    flag = True
                    break
        if flag:
            break
print count
