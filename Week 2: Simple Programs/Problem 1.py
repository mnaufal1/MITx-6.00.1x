'''
Write a program to calculate the credit card balance after one year if a person only pays the
minimum monthly payment required by the credit card company each month.

Several variables were defined by the course.

For each month, calculate statements on the monthly payment and remaining balance.
At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy.
'''

i = 12
while i > 0:
    minPay = balance * monthlyPaymentRate
    balance -= minPay
    interest = balance * (annualInterestRate/12)
    balance += interest
    i -= 1

print("Remaining balance: "+str(round(balance,2)))
