#CTI 110
#M5LAB_Debugging
#Michael Peters
#20 November 2017

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    # A_score = 100-90
    # B_score = 89-80
    # C_score = 79-70
    # D_score = 69-60
    # F_score = 59-0
    

    
    score = float(input('Enter number grade: '))


    if score == 100 or score >= 90:
        print('Your grade is: A')
        
    elif score >= 89 or score >= 80:
        print('Your grade is: B')
        
    elif score >= 79 or score >= 70:
        print('Your grade is: C')
        
    elif score >= 69 or score >= 60:
        print('Your grade is: D')
        
    elif score >= 59 or score == 0:
        print('Your grade is: F')

main()
