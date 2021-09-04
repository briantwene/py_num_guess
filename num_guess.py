#File: num_guess.py
#Author: Brian Twene(@bt521)
#Date: 02/09/2021

#import random module 
import random

#welcome function definiton
def main():
    #display a welcome message
    print("Welcome to the Number Guessing Game")
    #run the game when the user has pressed enter
    guessLogic()


#function for getting and validating user input
def getGuess():

    #get the users guess
    guess = input("Enter your guess here: ")

    #if the guess has anything other than number in the string then
    #keep asking the player until they put in valid info
    while not guess.isdecimal():
        #display valid message
        print("Invalid")
        #tell the user to enter another guess
        guess = input("Enter your guess here: ")
    print("\n")
    #once the input is valid then return the guess to the calling function
    return int(guess)

#function definition this handles the player playing the game
def guessLogic():
    #a boolean variable that states if the player wants to play a game 
    play = True
    #variable that counts the number of turns it takes to make the right guess
    turns = 0 
   
   #while the player wants to play
   # keep playing the game 
    while play == True:

        #generate a random number 
        mysteryNum = random.randint(1,10)
        #get the users guess
        guess = getGuess()
        #when the guess is entered this is counted as one turn
        turns += 1

        #while the guess doenst match
        while guess != mysteryNum:

            #check if the number is higher or lower
            if guess < mysteryNum:
                #give the player a hint
                print(guess,"is too low")
            else:
                print(guess,"is too high")
            #ask the user to guess again
            guess = getGuess() 
            #count it as a turn
            turns += 1

        #if the while has stopped, that means the user got it right
        print("you win, the mystery number is", mysteryNum)
        print("You did this in",turns,"turns\n")
        #reset the amount of turns to 0
        turns = 0

        #ask the user if they want to play again
        playAgain = input("want to try again? (y/n): ")
        if playAgain == "n":
            print("Alright, see ya!")
            play = False
            break

#run main
main()
