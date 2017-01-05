import numpy as np
class Display:
    def __init__(self, rows, columns):
        self.matrix = np.zeros( (rows, columns), dtype = int )
        self.rows = rows
        self.columns = columns
    
    def rotate_column(self, column, shift):
        self.matrix[:, column] = np.roll(self.matrix[:, column], shift, axis = 0)
        
    def rotate_row(self, row, shift):
        self.matrix[row, :] = np.roll(self.matrix[row,:], shift, axis = 0)
    
    def set_rect(self, A, B):
        assert A < self.rows and B < self.columns
        for i in xrange(A):
            self.matrix[i][0:B] = 1
    def count_pixels(self):
        return np.sum(self.matrix)
        
file = open("input.txt", 'r')
display = Display(6, 50)
for line in file:
    line = line.strip("\n")
    instruction = line.split(" ")
    if instruction[0] == "rect":
        a, b = map(int, instruction[1].split("x"))
        #print "%d, %d" %(a, b)
        display.set_rect(b, a)
    elif instruction[0] == "rotate":
        if instruction[1][0] == 'c':
            column = int(instruction[2].strip("x="))
            shift = int(instruction[4])
            display.rotate_column(column, shift)
        else:
            row = int(instruction[2].strip("y="))
            shift = int(instruction[4])
            display.rotate_row(row, shift)

m = display.matrix
for i in xrange(6):
    string = ""
    for j in xrange(50):
        if m[i][j] == 1:
            string += "#"
        else:
            string += "."
    print string
print "\n"


            
        
        
    