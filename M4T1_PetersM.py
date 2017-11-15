#CTI 110
#M4T1-Sales Prediction
#Michael Peters
#13 November 2017

#projected annual profit

totalSales=float(input('Enter Projected Sales: '))

#projected annual profit is 23%

annualProfit = totalSales * .23

#projected profit is rounded to the second decimal place

print("Projected Annual Profit is:" ,round(annualProfit,2))

#this is another way to round a decimal to the second place

#print("Projected Annual Profit is:" ,format(annualProfit,'.2f'))
