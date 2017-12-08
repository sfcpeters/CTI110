#CTI 110
#M7T2_FeetToInches
#Michael Peters
#4 December 2017

#program converts feet to inches


def feetToInches(userFeet):
    inches = (userFeet / 1) * 12
    return inches

def main():
    userFeet = float(input('Enter the number of feet?' ,))
    inches = feetToInches(userFeet)
    print(userFeet, ' feet is converted to' ,format(inches,'.2f') ,'inches')

    
main()
