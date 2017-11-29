#CTI 110
#M6HW2_Running Total
#Michael Peters
#28 November 2017

#adds together numbers then terminates on a negative number

total = 0
print('Program adds together positive numbers and will exit on negitive numbers')
number = float(input('Enter your first number;' ,))

while number > -1:
    total = total + number
    number = float(input('Enter your next number;' ,))

print('\nThe total of your numbers is' ,total)

