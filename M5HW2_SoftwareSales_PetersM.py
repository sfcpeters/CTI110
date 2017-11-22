#CTI 110
#M5HW2_SoftwareSales
#Michael Peters
#20 November 2017

# this program will account for a bulk discount on products sold

    #product is $99
    #4 discounts
    # 10% - 10-19 items sold
    # 20% - 20-49 items sold
    # 30% - 50-99 items sold
    # 40% - 100+ items sold
    
def main():

    totalPackages = float(input('total number of packages sold:' ,))
    subtotal = totalPackages * 99
    
    discount1 = subtotal * .1

    subtotal1 = subtotal - discount1
    
    discount2 = subtotal * .2

    subtotal2 = subtotal - discount2
    
    discount3 = subtotal * .3

    subtotal3 = subtotal - discount3
    
    discount4 = subtotal * .4

    subtotal4 = subtotal - discount4

    if totalPackages == 1 or totalPackages <= 9:
        
        print('total due:' ,format(subtotal,'.2f'))
                                  
    elif totalPackages <=10 or totalPackages <= 19:
        
        print('subtotal:' ,format(subtotal,'.2f'))

        print('10% discount:' ,format(discount1,'.2f'))

        print('total due:' ,format(subtotal1,'.2f'))
        
    elif totalPackages <=20 or totalPackages <= 49:

        print('subtotal:' ,format(subtotal,'.2f'))

        print('20% discount:' ,format(discount2,'.2f'))

        print('total due:' ,format(subtotal2,'.2f'))        

    elif totalPackages <=50 or totalPackages <= 99:

        print('subtotal:' ,format(subtotal,'.2f'))

        print('30% discount:' ,format(discount3,'.2f'))

        print('total due:' ,format(subtotal3,'.2f'))
    elif totalPackages <=100:

        print('subtotal:' ,format(subtotal,'.2f'))

        print('40% discount:' ,format(discount4,'.2f'))

        print('total due:' ,format(subtotal4,'.2f'))

main()
