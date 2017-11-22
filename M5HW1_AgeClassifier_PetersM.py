#CTI 110
#M5HW1_AgeClassifier
#Michael Peters
#20 November 2017

# this program will ask for a persons age and then classify them in an age group.

def main():
    
    # 4 catagories of age;
    # 0-1 infant
    # 2-12 child
    # 13-19 teenager
    # 20 and older an adult

    age = float(input('How old are you?' ,))

    
    if age == 0 or age == 1:
        print('You are an infant')
        
    elif age <= 2 or age <= 12:
        print('You are a child')
        
    elif age <= 13 or age <= 19:
        print('You are a teenager')
        
    elif age <= 20 or age <= 999999:
        print('You are an adult')

main()
    
