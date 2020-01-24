import matplotlib.pyplot
import untitled


num_of_agents = 25
# num_of_iterations = 500000
agents = []
environment = []
routeTracker = []
# environmentTracker = []
# Drunksoutput = []
iteration = 0


# Input the raster file
f = open("drunk.txt")
environment = []
for line in f:
    parsed_line = str.split(line,",")
# Returns a list of all the words in the string, using str as the separator
    rowlist = []
    for word in parsed_line:
        rowlist.append(float(word))
    environment.append(rowlist)
f.close()



# Highlight the pub area
for a in range(300):
   for b in range(300):
       if environment[a][b]==1:
          environment[a][b]=99
          


# Create this to show the density map, add value to where drunks have been
rows = len(environment[0])
cols = len(environment[0])
# print("len(environment)",len(environment))
# print("len(environment[0])",len(environment[0]))



# Make a 300*300 blank map
for row in range(rows):
    rowlist = []
    for col in range(cols):
        rowlist.append(0.0)
    routeTracker.append(rowlist)
    
    
'''
# Make the agents.
nrows = len(environment)
ncols = len(environment[0])

for row in range(nrows):
    for col in range(ncols):
        print(environment[row][col])
        if(environment[row][col] == 40):
            print("40 at row, col = ", row, col)
'''            


# Assign each agent a house number and starting position
for i in range(num_of_agents):#set house nuber as 10,20,30...
    houseNo = (i + 1) * 10
    agents.append((untitled.Agent(environment,agents,houseNo,routeTracker)))
    



#Continue moving and adding 1 to the environment tracker file until home
for i in range(num_of_agents):
    print (i)
    while agents[i].arrivedHome == False:
        #if agents[i].arrivedHome == False:
        agents[i].walk()
        #print("agents[i].y",agents[i].y)
        #print("agents[i].x",agents[i].x)
        #environmentTracker[agents[i].y][agents[i].x] +=1
        if agents[i].environment[agents[i].y][agents[i].x] == agents[i].houseNo:
            #agents[i].arrivedHome == True
            agents[i].arrivedHome = True
            print ("I am Home!",i,agents[i].x,agents[i].y)
            

        if (iteration == 5000):
            print("Plotting")
            matplotlib.pyplot.xlim(0, 300)
            matplotlib.pyplot.ylim(0, 300)
            matplotlib.pyplot.imshow(routeTracker)
            #sys.exit()
            #matplotlib.pyplot.show()
        iteration = iteration+1

fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(111)
matplotlib.pyplot.xlim(0,300)
matplotlib.pyplot.ylim(0,300)
matplotlib.pyplot.title('Drunks back home')

for m in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[m].x,agents[m].y)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()    



"""
f = open('Drunksoutput.csv', 'w', newline='') 
writer = csv.writer(f, delimiter=',')
for row in routeTracker:
    writer.writerow(row)


f = open('Drunksoutput.csv', newline='')
reader = csv.reader(f,delimiter=',')
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(int(value))
    environment.append(rowlist)
f.close()





reader = csv.reader(f,delimiter=',')
for row in routeTracker:
    writer.writerow(row)    
# Open file and read.
f = open('drunk.txt', newline='')
reader = csv.reader(f,delimiter=',')
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(int(value))
    environment.append(rowlist)
f.close()









        
#for j in range(num_of_iterations):
#    for i in range(num_of_agents):
#        agents[i].move()
#        agents[i].eat()
        
        





#for i in range (300):#indicates the number of columns
#    rowlist = []
#    for j in range (300):#indicates the number of rows
#        rowlist.append(0)
#    Drunksoutput.append(rowlist)         

fig=matplotlib.pyplot.figure(figsize = (10,10))
ax = fig.add_axes([0, 0, 1, 1])
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].i,agents[i].j)  
matplotlib.pyplot.show()

# Move the agents.
#trajectories = [[[],[]] for i in range(num_of_agents)]
#for j in range(num_of_iterations):
fig=matplotlib.pyplot.figure(figsize = (10,10))
ax = fig.add_axes([0, 0, 1, 1])
matplotlib.pyplot.xlim(0, 300)
matplotlib.pyplot.ylim(0, 300)
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

    

 












#ax = fig.add_axes([0, 0, 1, 1])
#    
#matplotlib.pyplot.imshow(Drunksoutput)
#matplotlib.pyplot.xlim(0, 300)
#matplotlib.pyplot.ylim(0, 300)
#matplotlib.pyplot.show()

'''
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
"""
