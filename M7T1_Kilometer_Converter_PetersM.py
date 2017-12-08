#CTI 110
#M7T1: Kilometer Converter
#Michael Peters
#4 December 2017

#program converts kilometers to miles

def askUser():
    kilometers = float(input('How many Kilometers have you traveled?' ,))
    return kilometers


def convertKilometers( kilometers):
    miles = kilometers * 0.6214
    return miles


def main():
    userKilometers = askUser()
    convertedMiles = convertKilometers(userKilometers)

    print(userKilometers, 'kilometers was converted to' \
          ,format(convertedMiles,'.2f'), 'miles')



main()
    
    
    
