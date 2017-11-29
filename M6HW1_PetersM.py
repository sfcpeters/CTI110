#CTI 110
#M6HW1_Distance Traveled
#Michael Peters
#28 November 2017


#calculates the time and distance a vehicle travels

#asking for user input
speed = float(input('What is the speed of the vehicle in mph?' ,))
hoursTraveled = int(input('How many hours has it traveled?' ,))

#output formulation
print('\nHour','\tDistance Traveled')
#if speed <= 0 or hoursTraveled <= 0:
    #print('Hours and mph have to be greater then 0')
    
for hour in range(1, hoursTraveled +1):
    distance = speed * hour
    print(hour,"\t",distance)
