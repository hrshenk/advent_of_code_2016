file = open("input.txt", "r")
compressed = file.read()
compressed = compressed.strip(" ")
compressed = compressed.strip("\n")
c_length = len(compressed)
decompressed = ""

i = 0
last = 0
string_array = []
while(i<c_length):
    if compressed[i] != '(':
        i += 1
    else:
        string_array.append(compressed[last:i])
        mark = ""
        i += 1
        while compressed[i] != ')':
            mark += compressed[i]
            i += 1
        i += 1
        char_count, multiplier = map( int, mark.split("x") )
        string_array.append( multiplier * compressed[i: (i + char_count)] )
        i += char_count
        last = i
decompressed = ''.join(string_array)
print len(decompressed)

        
        
        
    