#CTI 110
#M4HW2-Tip, Tax, and Total
#Michael Peters
#14 November 2017

# program to help calculte the total cost of a meal purchased
#custumer enters bill amount

subtotal=float(input('Enter total cost of food: '))

#bill amount is sub total
print('Subtotal:' ,(subtotal))

#Tax amount is 7%
salesTax = subtotal * .07

#amount is rounded
#print('sales tax' ,round(salesTax,2))

#amount is formated to the second decimal place
print('7% Sales Tax:' ,format(salesTax,'.2f'))

#tip amount is 18%
tip = subtotal * .18

#amount is rounded
#print('tip',round(tip,2))

#amount is formated to the second decimal place
print('18% Tip:',format(tip,'.2f'))

totalDue = subtotal + salesTax + tip

#amount is rounded
#print('total amount' ,round(totalDue,2))

#amount is formated to the second decimal place
print('Total Amount Due:' ,format(totalDue,'.2f'))
