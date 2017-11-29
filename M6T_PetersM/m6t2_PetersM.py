#CTI 110
#M6T2_Bug Collector
#Michael Peters
#27 November 2017

#program calculates the total of bugs collected for 7 days

total = 0

for day in range (1,8):
    
    print('Enter how many bugs collected on day' ,day)
    
    bugs = int(input())
    
    total+=bugs

print('you collected a total of' ,total, 'bugs in the last 7 days') 
