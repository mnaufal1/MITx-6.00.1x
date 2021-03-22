'''
Write a program that uses these bounds and bisection search to find the smallest monthly payment to the cent
(no more multiples of $10) such that we can pay off the debt within a year.
Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!).
Produce the same return value as you did in Problem 2.
'''

low = round(balance/12,2)
high = round((balance*(1+(annualInterestRate/12))**12) / 12, 2)
monthlyPayment = round((high + low) / 2.0, 2)
epsilon = 0.1

while True:
    tempBal = balance
    for i in range(12):
        tempBal -= monthlyPayment
        interest = tempBal * (annualInterestRate/12)
        tempBal += interest
    #Bisection Search implementation
    if abs(tempBal) <= epsilon:
        break
    elif tempBal < 0:
        high = monthlyPayment
    else:
        low = monthlyPayment
    monthlyPayment = round((high+low) / 2.0, 2)

print("Remaining balance: "+str(round(monthlyPayment,2)))
