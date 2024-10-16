# Name:     Karol Harasim
# Class:    CSC 110 spring 2024
# Project:  Programming project final
# Date:     4/29/2024

# Program Title:    Wordle

# Project description:
# --------------------
# This program will be a version ofthe game Wordle. The program will
# select a random 5 letter word from a dictionary then the player will have 6
# attempts to guess the correct word. After every guess the player makes the
# program will tell the player if the letters they guessed is not in the word,
# in the word but in the wrong position, or in the word in the right position.
# when the game is over the program will display the player's score and ask if
# they would like to play again.

# General solution
# ----------------
# Compare the player's word to the random word. Check if any of the letters from
# the player's word are in the guessed word, in the right spot, or not in the random
# word at all. Print the results back to the player. Repeat this 5 more times or until
# the player guesses the word. Return the player's score when the game is over.

# Pseudo code
# -----------
# prompt player to enter file name

# while play == True  
#   while guesses < 6 and found == False:

#       prompt player to make a guess

#       if letter is in correct position:
#           letter = green

#           if all letters == green:
#               found = True

#       if letter is in word but wrong position:
#           letter = yellow

#       else:
#           letter = X

#   if found == False
#       print answer

#   print score
#   ask player to play again

# Function design
# ---------------
import random
# first line in program (given)
# this will allow the program to select a random word

def openFile():
    # function to check to see if file exists
    # and open the file
    goodFile = False
    while goodFile == False:
        fname = input("Please enter a file name: ")
        try:
            dataFile = open(fname, "r")
            goodFile = True
        except IOError:
            print("Invalid file name try again ...")
    return dataFile

def makeCapital(word):
    # this function will take the player's guess
    # and make the letters in the word they type capital

    # make word into a list of letters
    lettersList = list(word)

    capitalWord = ''

    # loop to turn each letter capital
    for i in range(len(lettersList)):

        # get character value of letter then make it capital
        capital = ord(lettersList[i]) - 32
        capital = chr(capital)

        # add capital letter to capitalWord
        capitalWord += capital

    return capitalWord

def getPlayerWord(wordList):
    # This function will check if the word that the
    # player guesses is a valid word

    # loop that runs until player guesses a valid word
    good = False
     
    while good == False:

        # get guess word
        guess = input("Make a guess: ")
        
        # make word capital if it's lowercase
        testWord = list(guess)
        if ord(testWord[0]) >= 97 and ord(testWord[0]) <= 122:
            guess = makeCapital(guess)

        # linear search through wordList to see if the guess
        # word is in the list
        i = 0
        found = False
        while i < len(wordList) and found == False:

            # compare words
            if wordList[i] == guess:
                
                # if the guess is good the guess gets returned
                found = True
                good = True

            i += 1

        if found == False:
            print("Word not in dictionary - try again...")

    return guess


def getData():
    # This function uses the openFile() function to
    # get make a list of all the words in the file.
    # the function returns the list of words in the
    # dictionary
    
    # make wordList list
    wordList = []
    wordWorldList = []

    # open file
    infile = openFile()
    line = infile.readline()

    # loop to turn words in file into a list
    while line != "":
        line = line.strip()
        wordList.append(line)
        wordWorldList.append(line)
        line = infile.readline()

    #close file
    infile.close()

    return wordWorldList, wordList

def ranWord(wordList):
    # uses the randint function to find a random word
    # will use the wordList as a parameter so it can pick
    # a random word from the list. The function will return
    # the random word

    # get random number
    ranNum = round(random.randint(0,2498))

    # get word based of random number
    word = wordList[ranNum]

    return word


def computeClue(guessWord, worldWord):
	# this function gets the guess from the player and the 
    # random word as parameters. Then the function compares
    # the two words and returns the clues

    # initialize clue
    clue = ''
    
    # turn words into lists
    guessWord = list(guessWord)
    worldWord = list(worldWord)

    # check which letters are green, change matching letters
    # to 1
    guessWord = checkGreen(guessWord, worldWord)

    # check which letters are yellow, if letter is in wrong
    # position change the letter to 2
    guessWord, worldWord= checkYellow(guessWord, worldWord)

    # loop to assemble clue
    for i in range(len(guessWord)):
        
        # if the letter is in the correct spot clue is G
        if guessWord[i] == '1':
            clue += 'G'

        # if the letter is in the word but in the wrong spot
        # the clue is Y
        elif guessWord[i] == '2':
            clue += 'Y'

        # if the letter is wrong the clue is X
        else:
            clue += 'X'

    return clue

def checkGreen(guessWord, worldWord):
    # this function checks if the letters in the guessed
    # word are the correct letters in the correct spot

    # loop to check if letters are in the right spot
    for i in range(len(worldWord)):
            
        # if letters match, turn it into 1
        if worldWord[i] == guessWord[i]:
            guessWord[i] = '1'

            # change wordlWord letter to a number
            # so it can't be counted twice
            worldWord[i] = "0"
    
    
    return guessWord

def checkYellow(guessWord, worldWord):
    # this function checks if the letters in the guessed
    # word are the correct letters but in the wrong spot

    # nested loop to check if letter is in worldWord
    for i in range(len(worldWord)):
        for j in range(len(guessWord)):
            
            # if letter is in word turn into 2
            if worldWord[i] == guessWord[j]:
                guessWord[j] = '2'
                
                # change wordlWord letter to a number
                # so it can't be counted twice
                worldWord[i] = "0"

    return guessWord, worldWord



def main(seedIn):
    # the main function implements the functions defined above
    # also allows user to play again and keeps score
    
    # first line of code in main function (given)
    random.seed(seedIn)

    # get wordList
    wordWorldList, wordList = getData()

    # initialize score
    score = 0
    totalScore = 0

    # loop to let player play as long as they want
    play = True
    while play == True:

        # get random word
        worldWord = ranWord(wordWorldList)

        # loop 6 times or until player guesses correct word
        i = 0
        found = False
        while i < 6 and found == False:

            # get guess word
            guessWord = getPlayerWord(wordList)
            print(guessWord)

            # get clue
            clue = computeClue(guessWord, worldWord)
            print(clue)

            # check if guess was correct
            if clue == "GGGGG":
                found = True

            # increment score and i
            score += 1
            i += 1

        # makes it so the same word can't be chosen again
        #wordWorldList.remove(worldWord)

        # print results found
        if found == True:
            print('')
            print("Congratulations, your wordle score for this game is ", str(score))
        
        # print results not found
        elif found == False:
            print("Sorry, you did not guess the word: ", worldWord)
            score += 4

        # print total score
        totalScore += score
        print("Your overall score is ", str(totalScore))

        # reset score
        score = 0

        # ask to play again
        againPlay = False
        while againPlay == False:    
            print('')
            playAgain = input("Would you like to play again (Y or N)? ")

            # if player doesn't want to play again
            if playAgain == "N"or playAgain == 'n':
                play = False
                againPlay = True
                print('')
                print("Thanks for playing!")

            # if player does want to play again
            elif playAgain == "Y" or playAgain == "y":
                againPlay = True

            # wrong input
            else:
                print("Invalid input, try again")
                


                
    return

#main(2)

  





