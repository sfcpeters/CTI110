#CTI 110
#M5T1_AreasOfRectangles
#Michael Peters
#20 November 2017

# comparing the size of 2 rectanges to determine which is larger

def main():
    
    print('Rectangle 1')
    lengthA = float(input('what is the length of the first rectangle?' ,))
    widthA = float(input('what is the width of the first rectangle?' ,))
    areaA = lengthA * widthA

    print('Rectangle 2')
    lengthB = float(input('what is the length of the second rectangle?' ,))
    widthB = float(input('what is the width of the second rectangle?' ,))
    areaB = lengthB * widthB


    if areaA > areaB:
        print('The first rectangle has a larger area.')
        
    elif areaB > areaA:
        print('The second rectangle has a larger area.')
        
    elif areaA == areaB:
        print('Both rectangles have equal area.')
        
main()
