import re

def test_ABBA(string):
    for i in xrange( len(string)-3 ):
        print string[i]
        if ( string[i] != string[i+1] ) and ( string[i] == string[i+3] ) and ( string[i+1] == string[i+2] ):
            return True
    return False
        
file = open("input.txt", 'r')
count = 0
for line in file:
    flag = True
    line = line.strip("\n")
    m = re.split("[\[\]]", line)
    #due to structure of input, odd rows of m are 'hypernet' sequences
    #whence if any of them contain an ABBA we'll break from the loop
    for i in xrange(len(m)/2):
        if test_ABBA(m[2*i+1]):
            flag = False
            break
    #if no ABBA was found in the hypernet sequences then this is
    #eligible to be a TLS supporting IP.  Check for ABBA.
    if flag:
        for i in xrange(len(m)/2 + 1):
            if test_ABBA(m[2*i]):
                count += 1
                break
print count

