# Authur LeftBehind
# Made in Python3.10.2

import string
import random
import os

# A function to clean the console
cls = lambda: os.system('cls')
cls()
def game():
    cls()
    # Python3+ if you want to input your own source || file = input("What's the file location that you want to open? ")
    # Python2.7 || file = raw_input("What's the file location that you want to open? ")

    # file = "C://Users/niko7/Documents/Programming/hangman_WL.txt"

    # Make the file into a list and choose a random word
    # wordlist = open(file, "rt")
    # wordlist = wordlist.readlines()
    # word = random.choice(wordlist)
    
    guesses = 1
    guessC = 0

    wordlist = ["Hello","Olives","Mpampis","Catfish"]
    word = random.choice(wordlist)
    word = word.upper()
    
    firstchar = word[0]
    lastchar = word[-1]
    
    known = list(word)
    unknown = ["_"] * len(word)
    unknown[0] = firstchar
    unknown[-1] = lastchar
    
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

def start():

    play = input("Do you want to play a game of hangman?\n" + " [Y]es " + "[N]o :").lower()

    if play == "y":
        cls()
        game()
    elif play == "n":
        print("Ok nice seeing you!")
        cls()
    else:
        cls()
        print("Sorry invalid option!\n")
        start()

start()