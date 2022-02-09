# Authur LeftBehind
# Made in Python3.10.2

import string
import random
import os

# A function to clean the console
cls = lambda: os.system('cls')
cls()

def start():
    play = input("Do you want to play a game of hangman?\n" + " [Y]es " + "[N]o :").lower()
    if play == "y":
        cls()
        game()
    elif play == "n":
        cls()
        print("Ok nice seeing you!")
    else:
        cls()
        print("Sorry invalid option!\n")
        start()

def game():
    cls()
    # If you want to input your own source || file = input("What's the file location that you want to open? ")

    # Make the file into a list and choose a random word
    # wordlist = open(file, "r")
    # wordlist = wordlist.readlines()
    # word = random.choice(wordlist)
    
    # Setting some veriables
    guesses = 1
    guessC = 0
    
    # Getting the wordlist and choosing a random word as well as making all the letters capitals
    wordlist = ["Hello","Olives","Mpampis","Catfish"] # You can add your own words in here
    word = random.choice(wordlist)
    word = word.upper()
    
    # Setting the first and last character's of the word in thier own variables
    firstchar = word[0]
    lastchar = word[-1]
    
    # Setting the list's
    known = list(word)
    unknown = ["_"] * len(word)
    unknown[0] = firstchar
    unknown[-1] = lastchar
    
    # Telling the user the rule's of the game
    print("This is a game of hangman!\n")
    print("A random word is chosen and you have to guess the letters in it!\n")
    print("If you get 5 incorrect guesses, then you loose the game!\n")
    print("Good luck!\n")

    print(unknown)
    guess = input("Give me a letter: ").upper()
    cls()
    while "_" in unknown and guesses <= 5:
        guessC = 0
        for i in range(len(known)):
            if guess == known[i]:
                unknown[i] = guess
                print("Nice you guessed a letter!")
                guessC +=1
        if guessC == 0:
            guesses += 1
        if unknown == known:
            cls()
            print("Congratulations you won!!!")
            break
        print("Incorrect guesses:",guesses - 1)
        print(unknown)
        guess = input("Give me a letter: ").upper()
        cls()
    if guesses > 5:
        print("Game over!")
        
start()
