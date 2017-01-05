class Keypad:
    def __init__(self, m, n):
        self.keys = []
        self.focus = [m/2, n/2]
        for i in xrange(m):
            x = n*i
            self.keys.append([])
            for j in xrange(n):
                self.keys[i].append((x+1) + j)
            self.keys[x/m].append
            self.rows = m
            self.columns = n
            
    def enter_digit(self, line):
        for char in line:
            if (char == 'L') and (self.focus[1] != 0):
                self.focus[1] -= 1
            elif (char == 'R') and ( self.focus[1] != (self.columns - 1) ):
                self.focus[1] += 1
            elif (char == 'U') and (self.focus[0] != 0):
                self.focus[0] -= 1
            elif (char == 'D') and (self.focus[0] != (self.rows - 1) ):
                self.focus[0] += 1
        return self.keys[ self.focus[0] ][ self.focus[1] ]
                
        
file = open('input.txt', 'r')
keypad = Keypad(3,3)
i=0
for line in file:
    print keypad.enter_digit(line)
    
