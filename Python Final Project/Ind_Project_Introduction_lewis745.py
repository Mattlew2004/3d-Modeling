"""
===============================================================================
ENGR 13300 Fall 2023

Program Description
    My program is similar to an 80s style command prompt game.  My project takes in input and uses dice rolls and random inputs
    to kill monsters.  You can collect an item, with three different choices, each choice resulting in a different 
    outcome.  The player has a health value that, when 3 rolls are failed, causes the player to die.  The game is infintitely repeatable,
    so anyone testing can see all possible outcomes.  The program also displays pictures, that I drew, that show the monsters you are fighting.

Assignment Information
    Assignment:     Ind Project
    Author:         Matthew Lewis, lewis745@purdue.edu
    Team ID:        LC4 - 26 (e.g. LC1 - 01; for section LC1, team 01)

Contributor:    Matthew Lewis, lewis745@purdue.edu [repeat for each]
    My contributor(s) helped me:
    [x] understand the assignment expectations without
        telling me how they will approach it.
    [x] understand different ways to think about a solution
        without helping me plan my solution.
    [x] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.
    
ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""

# intro function that tells the user about the game and how to play
p_name = input("What is your character's name going to be?: ")
print(" ")
def intro():
    # Displays the introduction to the player
    print(f"Hello {p_name}, welcome to Dungeon Masters!\n"
          "In this game, you will defeat monsters and collect items. A certain item is needed to defeat the boss at the end.")
    print("Using a D10, you will start with 3 hearts, with each failed roll against a monster resulting in a heart of damage.")
    input("Alright, get out there and clear the dungeon!\nPress anything to begin!: ")
    print(" ")