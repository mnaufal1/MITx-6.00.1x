'''
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

Several variables were defined by the course.

Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made).
The monthly payment must be a multiple of $10 and is the same for all months.
'''

monthlyPayment = 10
tempBal = balance

while tempBal > 0:
    tempBal = balance
    for i in range(12):
        tempBal -= monthlyPayment
        interest = tempBal * (annualInterestRate/12)
        tempBal += interest
    if tempBal > 0:
        monthlyPayment += 10

print("Remaining balance: "+str(monthlyPayment))
