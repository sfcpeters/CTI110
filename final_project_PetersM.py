#CTI 110
#finalproject
#Michael Peters
#11 December 2017


#this is a rock paper scissors game


import random

def userName():
    
    name = input('Please enter your name:' ,)
    
    return name


def generateRandomNumber():
    
    randomNumber = random.randint(1,3)
    
    return randomNumber


def getComputerChoice(randomNumber):
    
    if randomNumber == 1:
        computerChoice = 'rock'
        
    elif randomNumber == 2:
        computerChoice = 'paper'
        
    elif randomNumber == 3:
        computerChoice = 'scissors'

    return computerChoice


def getUserChoice():
    
    userChoice = input('Please enter your choice:' ,)
    
    return userChoice

def determineWinner(computerChoice, userChoice):
    
    rockMessage = 'rock smashes scissors'
    scissorsMessage = 'scissors cuts paper'
    paperMessage = ' paper covers rock'
    winner = 'no winner'
    message = ''

    if computerChoice == 'rock' and userChoice == 'scissors':
        winner = 'Computer'
        message = rockMessage
        
    elif computerChoice == 'scissors' and userChoice == 'rock':
        winner = 'Player'
        message = rockMessage
        
    if computerChoice == 'scissors' and userChoice == 'paper':
        winner = 'Computer'
        message = scissorsMessage
        
    elif computerChoice == 'paper' and userChoice == 'scissors':
        winner = 'Player'
        message = scissorsMessage

    if computerChoice == 'paper' and userChoice == 'rock':
        winner = 'Computer'
        message = paperMessage
        
    elif computerChoice == 'rock' and userChoice == 'paper':
        winner = 'Player'
        message = paperMessage

    return winner, message


def startAgain():

   
    randomNumber = generateRandomNumber()
    computerChoice = getComputerChoice(randomNumber)
    userChoice = getUserChoice()
    print('The computer chose' , computerChoice)
    winner, message = determineWinner(computerChoice, userChoice)

    if winner != 'no winner':
        print(winner, 'won(' ,message, ')')

    return winner

def tryAgain():
    
    choice = input('Would you like to play again? y/n:' ,)
    
    if choice == 'y' or choice == 'yes' or choice == 'Y':
        main()
        
    elif choice == 'n' or choice == 'no' or choice == 'N':
        print ('Thanks for playing')
        quit()
        
    else:
        print ('Try again')
        tryAgain() 


def main():
    
    print('Would you like to play rock, paper,scissors game, a number guessing game,\n or a word guessing game?')
    pick = input(' 1 for the rock,paper,scissors game, 2 for the number guessing game, \n or 3 for the word guessing game: 1 /2 / 3?' ,)
    
    if pick == '1':
        name = userName()
        print ('Please choose paper, rock or scissors')
        randomNumber = generateRandomNumber()
        computerChoice = getComputerChoice(randomNumber)
        userChoice = getUserChoice()
        print('The computer chose' ,computerChoice)
        winner, message = determineWinner(computerChoice, userChoice)

        if winner != 'no winner':
            print(winner, 'won(' ,message, ')')

        while winner == 'no winner':
            print ('Tie Game, Try Again' ,winner)
            winner = startAgain()
            
        tryAgain()
        
    elif pick == '2':
        
        name = input ('What is your name?' ,)
        number = random.randint(1, 1000)

        print( 'Hello ' + name + ',You have 10 guesses to determine a number between 1 and 1000')
        #print (number)
        guessTaken = 0

        while guessTaken < 10:
            guess = input('What is your guess?' ,)
            guess = int (guess)
            
            if guess < number:
                print('Your guess was to low')
                
            elif guess > number:
                print ('Your guess was to high')
                
            else:
                break
            
            guessTaken = guessTaken + 1
            
        if guess == number:
            print ('You have guessed the number in' , guessTaken)
            
        else:
            print ('You have not guessed the number which was' , number)

        tryAgain()

    elif pick == '3':
        wordbank = ['elf','dasher','dancer','prancer','vixen','comet',\
        'stocking','donner','blixen','rudolph','christmas','snowman',\
        'gingerbread','cookies','santa','presents','reindeer','sleigh',\
                    'icicle','holiday','frosty']
        name = input('What is your name?')
        print ('Hello' , name, 'Time to play guess the Christmas word.')
        print ('Start guessing...')
        word = random.choice(wordbank)
        #print (word)
        guesses = ''
        turns = 10
        
        while turns > 0:          
            failed = 0
            
            for char in word:
                
                if char in guesses:    
                    print (char,)
                    
                else:
                    print ('?')     
                    failed += 1
                    
            if failed == 0:        
                print ('You won')  
                break
            
            guess = input('guess a letter:' ,) 
            guesses += guess
            
            if guess not in word:  
                turns -= 1        
                print ('Wrong')
                print ('You have' ,turns, 'more guesses')
                
            if turns == 0:           
               print ('You Lose')
               print (word)
               
        tryAgain()
        
    else:
        print ('Try again')
        main()


main()

