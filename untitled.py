import random

class Agent():
    def __init__(self, environment, agents, houseNo,routeTracker):
        self.environment = environment
        self.agents = agents
        self.houseNo = houseNo
        self.x = random.randint(137,157)
        self.y = random.randint(127,147)
        self.arrivedHome = 0
        self.routeTracker = routeTracker 
    def walk(self):
        #for agents in self.agents:
        if self.arrivedHome == 0:
             if random.random() < 0.5:
                 self.x = (self.x + 5)%300
             else:
                 self.x = (self.x - 5)%300
             if random.random() < 0.5:
                self.y = (self.y + 5)%300
             else:
                self.y = (self.y - 5)%300    
        #add value to the routeTracker
        #get the value of routeTracker at x,y
        '''value = self.routeTracker[self.y][self.x]
        #add 1 to this value
        value2 = value + 1
        #store this new value in environmtTracker
        self.routeTracker[self.y][self.x] = value2'''
        
        self.routeTracker[self.y][self.x] = self.routeTracker[self.y][self.x]+1
        
    def distance_between(agents_row_a, agents_row_b):
        return (((agents_row_a[0] - agents_row_b[0])**2) +
        ((agents_row_a[1] - agents_row_b[1])**2))**0.5        
                
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] >= 0:
            self.environment[self.y][self.x] += 50
   