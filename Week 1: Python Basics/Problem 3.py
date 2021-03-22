'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.

For example, if s = 'azcbobobegghakl', then your program should print:

    Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:

    Longest substring in alphabetical order is: abc
'''

substr = ""
temp = ""
i = 0

while i+2 < len(s):
    #checks if the next letter is not in alphabetical order to the current letter
    #if condition is true, skips to next iteration
    if s[i] > s[i+1]:
        i += 1
    #checks if it is in order, if so then it checks how many letters are in order
    #also adds to the substr variable the ones in order
    elif s[i] <= s[i+1]:
        while s[i] <= s[i+1]:
            substr += s[i]
            i += 1
            #breaks the loop if out of range
            if i+1 == len(s):
                break
        #flaw in my code, this is for adding on the last letter if its in order
        #I did not figure out a way to do this previously without having out of bounds error
        if s[i] >= s[i-1]:
            substr += s[i]
    if len(substr) > len(temp):
        temp = substr
    substr = ""
if temp == "":
    temp = s[0]
    
print("Longest substring in alphabetical order is: " + temp)
