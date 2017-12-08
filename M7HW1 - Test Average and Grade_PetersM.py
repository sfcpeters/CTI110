#CTI 110
#M7HW1 - Test Average and Grade
#Michael Peters
#4 December 2017

#calculates the test averages and the grade

def calcAverage(test1, test2, test3, test4, test5, test6, test7, test8, test9):
    average = (test1 + test2 + test3 + test4 + test5 + test6 + test7 + test8 + test9) / 9
    return average

def determineGrade(score):
    if(score == 100 or score >= 90):
        return 'A'
    elif(score >= 89 or score >= 80):
        return 'B'
    elif (score >= 79 or score >= 70):
        return 'C'
    elif (score >= 69 or score >= 60):
        return 'D'
    elif (score <= 59 or score == 0):
        return 'F'

def getTestScore():
    test1 = float(input('Input test score 1:' ,))

    test2 = float(input('Input test score 2:' ,))

    test3 = float(input('Input test score 3:' ,))

    test4 = float(input('Input test score 4:' ,))

    test5 = float(input('Input test score 5:' ,))

    test6 = float(input('Input test score 6:' ,))

    test7 = float(input('Input test score 7:' ,))

    test8 = float(input('Input test score 8:' ,))

    test9 = float(input('Input test score 9:' ,))

    return test1, test2, test3, test4, test5, test6, test7, test8, test9

def printResults(test1, test2, test3, test4, test5, test6, test7, test8, test9):
    print ('Score\tGrade')
    print (str(test1) + '\t' + determineGrade(test1))
    print (str(test2) + '\t' + determineGrade(test2))
    print (str(test3) + '\t' + determineGrade(test3))
    print (str(test4) + '\t' + determineGrade(test4))
    print (str(test5) + '\t' + determineGrade(test5))
    print (str(test6) + '\t' + determineGrade(test6))
    print (str(test7) + '\t' + determineGrade(test7))
    print (str(test8) + '\t' + determineGrade(test8))
    print (str(test9) + '\t' + determineGrade(test9))
           
                  
def main():
    test1, test2, test3, test4, test5, test6, test7, test8, test9 = getTestScore()
   
    printResults(test1, test2, test3, test4, test5, test6, test7, test8, test9)

    print( "Your average is", calcAverage ( test1, test2, test3, test4, test5, test6, test7, test8, test9 ) )

main()
                  

