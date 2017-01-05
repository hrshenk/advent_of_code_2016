class bot:
    def __init__(self, id_num):
        self.id_num = id_num
        self.instructions = {}
        self.values = []
        self.count = 0
        self.factory = None
        self.watch_pair = []
        
    def receive_instructions(self, low, high):
        self.instructions["low"] = low
        self.instructions["high"] = high
        
    def receive_value(self, val):
        self.values.append(val)
        self.count += 1
        if self.count == 2:
            if self.watch_pair == sorted(self.values):
                print "bot %d compared %d and %d" %(self.id_num, self.watch_pair[0], self.watch_pair[1])
            self.handoff()
                
    def handoff(self):
        low = min(self.values)
        high = max(self.values)
        if self.instructions["low"][0] == "bot":
            self.factory.bots[self.instructions["low"][1]].receive_value(low)
        else:
            self.factory.containers[ self.instructions["low"][1] ] = low
        
        if self.instructions["high"][0] == "bot":
            self.factory.bots[ self.instructions["high"][1] ].receive_value(high)
        else:
            self.factory.containers[ self.instructions["high"][1] ] = high
        self.values = []
        
    def add_watch_pair(self, val1, val2):
        self.watch_pair.append( min(val1,val2) )
        self.watch_pair.append( max(val1, val2) )
        

class factory:
    def __init__(self, bot_count):
        self.bots = []
        self.containers = {}
        self.count = bot_count
        self.init_values = []
        for i in xrange(self.count):
            new = bot(i)
            new.factory = self
            self.bots.append(new)
        
    
    def load_instructions(self, instructions):
        self.loaded = True
        for line in instructions:
            line = line.strip("\n")
            if line[0] == 'v':
                a = line.split(" ")
                v, b = int(a[1]), int(a[5])
                self.init_values.append( (v,b) )
            else:
                a = line.split(" ")
                b = int( a[1] )
                assert (0 <= b and b < self.count)
                low = [ a[5], int( a[6] ) ]
                assert (0 <= low[1] and low[1] < self.count)
                high = [ a[10], int( a[11] ) ]
                assert (0 <= high[1] and high[1] < self.count)
                self.bots[b].receive_instructions(low, high)
        
    def execute_instructions(self):
        for val, bot in self.init_values:
            self.bots[bot].receive_value(val)
    
    def add_watch_pair(self, val1, val2):
        for bot in self.bots:
            bot.add_watch_pair(val1, val2)
            
                
f = factory(250)
file = open("input.txt", "r")
f.load_instructions(file)
f.execute_instructions()
h = f.containers
print h[0]*h[1]*h[2]
        
        