class Keypad:
    def __init__(self):
        self.keys = []
        self.keys.append([0,0,0,0,0,0,0])
        self.keys.append([0,0,0,1,0,0,0])
        self.keys.append([0,0,2,3,4,0,0])
        self.keys.append([0,5,6,7,8,9,0])
        self.keys.append([0,0,10,11,12,0,0])
        self.keys.append([0,0,0,13,0,0,0])
        self.keys.append([0,0,0,0,0,0,0])
        self.focus = [1, 3]
        
    def enter_digit(self, line):
        m, n = self.focus
        for char in line:
            if (char == 'L') and (self.keys[m][n-1] != 0):
                n -= 1
            elif (char == 'R') and ( self.keys[m][n+1] ):
                n += 1
            elif (char == 'U') and (self.keys[m-1][n] != 0):
                m -= 1
            elif (char == 'D') and (self.keys[m+1][n] ):
                m += 1
            self.focus = [m, n]
        return self.keys[ self.focus[0] ][ self.focus[1] ]

file = open('input.txt', 'r')
keypad = Keypad()
for line in file:
    print "%x" %( keypad.enter_digit(line) )