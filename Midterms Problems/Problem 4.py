'''
Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters. For example, if aList = ["apple", "cat", "dog", "banana"],
your function should return: ["cat", "dog"]
'''

def lessThan4(aList):
    bList = []
    
    for thing in aList:
        if len(thing) < 4:
            bList.append(thing)
    
    return bList
