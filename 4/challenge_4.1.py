file = open("input.txt", 'r')
count = 0
j = 0
for line in file:
    j += 1
    brack = line.rindex("[")
    dash = line.rindex("-")
    check_sum = line[brack:]
    check_sum = check_sum.replace("[", "")
    check_sum = check_sum.replace("]", "")
    string = line[0:dash]
    sector_id = int(line[dash+1:brack])
    string = string.replace("-", "")
    h = {}
    for char in string:
        if h.has_key(char):
            h[char] += 1
        else:
            h[char] = 1
    new_sum = ""
    i = 0
    for key, value in sorted(h.iteritems(), key=lambda (k,v): (-v,k)):
        new_sum += key
        i += 1
        if i == 5:
            break
    if check_sum[0:5] == new_sum[0:5]:
        count += sector_id
        
print count