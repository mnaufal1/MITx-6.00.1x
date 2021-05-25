'''
Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer.
Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.
'''

import string
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    mistakesCount = 8
    lettersGuessed = []
    
    print("Welcome to the game Hangman!")
    print("The secret word contains "+str(len(secretWord))+" words.")
    print("-----------")

    while mistakesCount > 0:
        print("You have "+str(mistakesCount)+" guesses remaining!")
        print("Available Letters: "+getAvailableLetters(lettersGuessed))
        userGuess = input("Please guess a letter: ").lower()
        if userGuess in lettersGuessed:
            lettersGuessed.append(userGuess)
            print("Oops! You've already guessed that letter: "+getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
        elif userGuess in secretWord:
            lettersGuessed.append(userGuess)
            print("Good guess: "+getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
        else:
            lettersGuessed.append(userGuess)
            print("Oops! That letter is not in my word: "+getGuessedWord(secretWord, lettersGuessed))
            print("-----------")
            mistakesCount -= 1
        if isWordGuessed(secretWord, lettersGuessed):
            return "Congratulations, you won!"
        if mistakesCount == 0:
            return "Sorry, you ran out of guesses. The word was "+secretWord+"."
            return "Congratulations, you won!"
