file = open("input.txt", 'r')
for line in file:
    dash = line.rindex("-")
    sector_id = int(line[dash+1:dash+4])
    text = line[:dash]
    ordinals = map(ord, text.replace("-", " "))
    string = ""
    for char in ordinals:
        if char != 32:
            char = ( (char-97 + sector_id) % 26 ) + 97
            string += chr(char)
        else:
            string += " "
    if string.find("pole") != -1:
        print string
        print sector_id

