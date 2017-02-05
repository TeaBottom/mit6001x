# # MITx: 6.00.1x Problem Set 3
# Purpose: Interactive game of hangman

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = ''
    for char in secretWord:
        if char in lettersGuessed:
            guessedWord += char
        else:
            guessedWord += '_ '
    return guessedWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    availableLetters = ''
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            availableLetters += letter
    return availableLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.
    '''
    # Game startup prompt
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")

    # Declare variable outside game loop
    lettersGuessed = []
    gameOver = False
    numGuesses = 8

    #Game loop
    while not gameOver:
        # Update available letters
        availableLetters = getAvailableLetters(lettersGuessed)

        # Introduction prompt
        print("-------------")
        print("You have " + str(numGuesses) + " guesses left")
        print("Available letters: " + availableLetters)
        guess = raw_input("Please guess a letter: ").lower()

        # Check if letter wasn't guessed then add it
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + guessedWord)
            continue
        else:
            lettersGuessed += guess

        # Display whether or not user guessed a correct letter & update number of guesses
        guessedWord = getGuessedWord(secretWord, lettersGuessed)
        if guess in guessedWord:
            print("Good guess: " + guessedWord)
        else:
            print("Oops! That letter is not in my word: " + guessedWord)
            numGuesses -= 1

        # Check game status
        gameOver = isWordGuessed(secretWord, lettersGuessed)
        if numGuesses == 0:
            gameOver = True

    # Display whether user won or lost
    print("-------------")
    if guessedWord == secretWord:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
