#CTI 110
#M7HW2_GuessingGame
#Michael Peters
#4 December 2017


#this is a random number guessing game


import random

def generateRandomNumber():
    randomNumber = random.randint(1, 100)
    return randomNumber

def askUserForNumber(message = 'Guess the Number:' ,):
    userNumber = int(input(message))
    return userNumber

def checkUserNumber(userNumber, randomNumber):
    if userNumber > randomNumber:
        return 'Too High'
    elif userNumber < randomNumber:
        return 'Too Low'
    else:
        return 'Congratulations!'


def main():

    userCongratulated = False
    letsStart = True

    while userCongratulated or letsStart:

        guesses = 0
        randomNumber = generateRandomNumber()
        userNumber = askUserForNumber()
        guesses = guesses + 1
        message = checkUserNumber(userNumber, randomNumber)

        while message != 'Congratulations!':
            print(message)
            userNumber = askUserForNumber('Try Again:' ,)
            guesses = guesses + 1
            message = checkUserNumber(userNumber, randomNumber)


        print (message, ' You took' ,guesses, 'guesses.\n')
        userCongratulated = True


main()
    
