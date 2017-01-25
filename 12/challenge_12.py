file = open("input.txt", "r")
instructions = [line.strip("\n").split() for line in file]
ip = 0; a = 0; b = 0; c = 1; d = 0
h = { 'a':a, 'b':b, 'c':c, 'd':d }
while ip < len(instructions):
    i = instructions[ip]
    if i[0] == "cpy":
        if not h.has_key(i[1]):
            h[i[2]] = int(i[1])
        else:
            h[i[2]] = h[i[1]]
        ip += 1
    elif i[0] == "inc":
        h[i[1]] += 1
        ip += 1
    elif i[0] == "dec":
        h[i[1]] -= 1
        ip += 1
    elif i[0] == "jnz":
        if not h.has_key(i[1]):
            if int(i[1]) != 0:
                ip += int(i[2])
            else:
                ip += 1
        elif h[i[1]] != 0:
            ip += int(i[2] )
        else:
            ip += 1
    else:
        ip += 1
        
print h['a']
    
