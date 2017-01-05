import re
file = open("input.txt", "r")
compressed = file.read()
c_length = len(compressed)

def get_expand_len(string, length, multiplier):
    #if the string has no tags then return length times multiplier
    if re.search("(\([0-9]+x[0-9]+\))", string) == None:
        return length*multiplier
    i, j, count = 0, 0, 0
    while i < length:
        if re.match("(\([0-9]+x[0-9]+\))", string[i:]):
            j = i + 1
            while string[i] != ')':
                i+=1
            l, m = map(int, string[j:i].split("x"))
            i += 1
            count += get_expand_len(string[i:i+l], l, m)
            i += l
        else:
            count += 1
            i += 1
    return count * multiplier
print get_expand_len(compressed, c_length, 1)


    