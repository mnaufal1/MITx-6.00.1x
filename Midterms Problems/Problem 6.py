'''
Write a function called gcd that calculates the greatest common divisor of two positive integers.
The gcd of two or more integers, when at least one of them is not zero, is the largest positive integer that divides the numbers without a remainder.
'''

def gcd(a, b):
    '''
    a, b: positive integers
    
    Returns the greatest common divisor of a & b
    '''
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
