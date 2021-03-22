'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.

For example, if s = 'azcbobobegghakl', then your program should print:

    Number of times bob occurs is: 2
'''

length = len(s)
bobCount = 0
iteration = 0
if "bob" in s:
    for x in s:
        if s[iteration:iteration+3] == "bob":
            bobCount += 1
        iteration += 1
print("Number of times bob occurs is: "+str(bobCount))
