#CTI 110
#M6HW3_Factorial
#Michael Peters
#28 November 2017

#calculates the factorial of a number

userNumber = int(input('enter your number:' ,))

while userNumber <1:
    userNumber = int(input('enter a positive number:' ,))

factorial = 1

for currentNumber in range(1,userNumber + 1):
    factorial = factorial * currentNumber

print('\nThe factorial of' ,userNumber,'is' ,factorial)
