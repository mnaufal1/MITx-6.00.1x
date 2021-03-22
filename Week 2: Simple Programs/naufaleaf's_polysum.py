"""
EdX MIT Course Excercise, Polysum

@author: naufaleaf
"""

import math

def polysum(n,s):
    '''
    Input two string or float, n = number of sides of polygon and s = length of sides
    Returns the sum of area of the polygon and perimeter
    '''
    area = (0.25 * n * s**2) / (math.tan(math.pi / n))
    perimeter = n * s
    
    sum = area + perimeter**2
    
    return round(sum, 4)