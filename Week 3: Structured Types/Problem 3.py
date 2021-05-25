'''
Next, implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. This function returns a string that is comprised of lowercase
English letters - all lowercase English letters that are not in lettersGuessed.
'''

import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = ""
    for char in string.ascii_lowercase:
        if char not in lettersGuessed:
            availableLetters += char
    return availableLetters
