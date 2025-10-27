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


# Imports the necessary libraries
import random
import cv2
from Ind_Project_Introduction_Mattlew2004 import intro

# Declares the health variable before all else
health = 3

# Main function that structures and runs all of most of the code
def Main():
    intro()
    for room in rooms:
        room()
    repeat()

# room_1 function that displays a picture and attacks a monster using a random roll
def room_1():
    global health
    # Displays an image of the skeleton from a separate file
    skele_image = cv2.imread('skeleton.png', cv2.IMREAD_ANYCOLOR)
    cv2.imshow('A horrifying skeleton!', skele_image)
    cv2.waitKey(4000)
    cv2.destroyAllWindows()
    
    print("In the first room, a skeleton attacks!\nYou must roll a 2 or above out of 10 to defeat him.")

    # Creates a random value from 1 to 10
    rand_roll_r1 = random.randint(1,10)
    # Asks for input on a roll
    print(input("What will you roll... (press anything to continue): "))
    print(f"You rolled a {rand_roll_r1}!")
    # An if statement that says whether your roll falls in range or you take damage
    if rand_roll_r1 in range(2,11):
        print("You killed the skeleton! Well done!")
    else:
        # Health is decreased when you lose a roll
        health -= 1
        print(f"You take 1 heart of damage! You have {health} hearts remaining!")
        # When your health is below or equal to 0 you die
        if health <= 0:
            print("You have died a gruesome death!\nTHANKS FOR PLAYING!\n")
            repeat()
            exit()
    
    print("You move to the next room...\n")
    cv2.waitKey(4000)

# room_2 function that displays a picture and attacks a monster using a random roll
def room_2():
    global health
    # Displays an image of the rat from a separate file
    rat_image = cv2.imread('rat.png', cv2.IMREAD_ANYCOLOR)
    cv2.imshow('A horrifying caustic rat!', rat_image)
    cv2.waitKey(4000)
    cv2.destroyAllWindows()

    print("In the second room, a large caustic rat attacks!\nYou must roll a 4 or above out of 10 to defeat him.")

    # Creates a random value from 1 to 10
    rand_roll_r2 = random.randint(1,10)
    # Asks for input on a roll
    print(input("What will you roll... (press anything to continue): "))
    print(f"You rolled a {rand_roll_r2}!")
    # An if statement that says whether your roll falls in range or you take damage
    if rand_roll_r2 in range(4,11):
        print("You killed the caustic rat! Well done!")
    else:
        # Health is decreased when you lose a roll
        health -= 1
        print(f"You take 1 heart of damage! You have {health} hearts remaining!")
        # When your health is below or equal to 0 you die
        if health <= 0:
            print("You have died a gruesome death!\nTHANKS FOR PLAYING!\n")
            repeat()
            exit()

    print("You move to the next room...\n")
    cv2.waitKey(4000)

# room_3 function that displays a picture and attacks a monster using a random roll
def room_3():
    global health
    # Displays an image of the eyeballs from a separate file
    eyeballs_image = cv2.imread('eyeballs.png', cv2.IMREAD_ANYCOLOR)
    cv2.imshow('A horrifying pair of eyeballs!', eyeballs_image)
    cv2.waitKey(4000)
    cv2.destroyAllWindows()

    print("In the third room, you see a pair of floating eyeballs, yuck!\nYou must roll a 5 or above for each eyeball to defeat them.")

    # Creates a random value from 1 to 10
    rand_roll_r3_eye_1 = random.randint(1,10)
    # Asks for input on a roll
    print(input("What will you roll... (press anything to continue): "))
    print(f"You rolled a {rand_roll_r3_eye_1}!")
    # An if statement that says whether your roll falls in range or you take damage
    if rand_roll_r3_eye_1 in range(5,11):
        print("You killed the first eyeball! Well done! Now kill the other one!")
    else:
        # Health is decreased when you lose a roll
        health -= 1
        print(f"You take 1 heart of damage! You have {health} hearts remaining!")
        # When your health is below or equal to 0 you die
        if health <= 0:
            print("You have died a gruesome death!\nTHANKS FOR PLAYING!\n")
            repeat()
            exit()

    # Creates a random value from 1 to 10
    rand_roll_r3_eye_2 = random.randint(1,10)
    # Asks for input on a roll
    print(input("What will you roll... (press anything to continue): "))
    print(f"You rolled a {rand_roll_r3_eye_2}!")
    # An if statement that says whether your roll falls in range or you take damage
    if rand_roll_r3_eye_2 in range(5,11):
        print("You killed the second eyeball! Well done!")
    else:
        # Health is decreased when you lose a roll
        health -= 1
        print(f"You take 1 heart of damage! You have {health} hearts remaining!")
        # When your health is below or equal to 0 you die
        if health <= 0:
            print("You have died a gruesome death!\nTHANKS FOR PLAYING!\n")
            repeat()
            exit()
    print("You move to the next room...\n")
    cv2.waitKey(4000)

# item_room function that displays a picture and allows the user to choose a certain item
def item_room():
    # Displays an image of the items from a separate file
    items_image = cv2.imread('items.png', cv2.IMREAD_ANYCOLOR)
    cv2.imshow('Some items to choose from!', items_image)
    cv2.waitKey(4000)
    cv2.destroyAllWindows()

    print("In the fifth room, you find 3 item pedastals, each with a different item to choose between.\n")
    global chosen_item
    # Asks the user to choose an item the mirror, the battle axe, or the bowl of spaghetti
    chosen_item = input("Which item will you choose, the mirror, the battle axe, or the bowl of spaghetti? (answer m, ba, or bs): ")
    # This code will loop when chosen_item does not equal bs, ba, or m
    while chosen_item != "bs" or chosen_item != "ba" or chosen_item != "m":
        # User chose the bowl of spaghetti
        if chosen_item == "bs":
            print("Alright, you have chosen the bowl of spaghetti!\n")
            break
        # User chose the battle axe
        elif chosen_item == "ba":
            print("Alright, you have chosen the battle axe!\n")
            break
        # User chose the mirror
        elif chosen_item == "m":
            print("Alright, you have chosen the mirror!\n")
            break
        else:
        # If the user input an incorrect value, the while loop will ask and run again
            print("Please choose an item.\n")
            chosen_item = input("Which item will you choose, the mirror, the battle axe, or the bowl of spaghetti? (answer m, ba, or bs): ")
    cv2.waitKey(4000)

# The final room where you can choose to either use your selected item or not with outcomes that differ based on choice
def boss_room():
    # Displays an image of the boss from a separate file
    boss_image = cv2.imread('boss.png', cv2.IMREAD_ANYCOLOR)
    cv2.imshow('The horrifying Gorloch the All-Seeing Eye!', boss_image)
    cv2.waitKey(4000)
    cv2.destroyAllWindows()

    print("You have made it to the boss room! Gorloch the All-Seeing Eye is your mighty foe!\nQuickly, use the item you collected and put this loser in a glau-coma!")
    # Asks the user if they want to use their item
    using_item = input("Use your item on this freak? (Y/N): ")
    # This code will loop when using_item does not equal Y or N
    while using_item != "Y" or using_item != "N":
        if using_item == "Y":
            # If the mirror is chosen and used you win!
            if chosen_item == "m":
                print("\nUsing the mirror, you reflect a beam of sunlight peering from a crack in the floor above directly into his eye!\nHe shrivels up, and you are victorious!\n"
                    "\nTHANK YOU FOR PLAYING!")
                break
            # If the battle axe is chosen and used you lose
            elif chosen_item == "ba":
                print("\nUsing the battle axe, you run at the beast and get one good slice in before he smashes you 6 feet under. You die in a pool of blood, sweat, and defeat.\n"
                    "\nTHANK YOU FOR PLAYING!")
                break
            # If the bowl of spaghtti is chosen and used you lose
            elif chosen_item == "bs":
                print('\nYou fling the bowl of spaghetti at the monster, and then realize your mistake in item choice as he makes the room look like a Party City with your intestines.\nThe locals will remember you as the "idiot spaghetti guy".\n'
                    "\nTHANK YOU FOR PLAYING!")
                break
        # If the user chooses to not use their item, they will die
        elif using_item == "N":
            print("\nYou decide that your pitiful item isn't fit for the likes of a manly man such as yourself, so you go in swinging your fists wildly.\n"
                "Gorloch lets out a hardy laugh before kneeding your body like dough (you die horribly).\n"
                "\nTHANK YOU FOR PLAYING!")
            break
        else:
        # While loop will repeat when Y or N is not the input value
            print("Error: Please enter either 'Y' or 'N'.")
            using_item = input("Use your item on this freak? (Y/N): ")
            print(" ")

# Repeats the game to allow you to see all outcomes or find the correct item choice
def repeat():
    # Asks the user if they want to play again
    x = input("Do you want to play or play again? (Y/N): ")
    print(" ")
    # This code will repeat as long as x is not equal to Y or N
    while x != "Y" or x != "N":
        if x == "Y":
            cv2.destroyAllWindows()
            # The code will repeat itself from the beginning
            Main()
        elif x == "N":
            cv2.destroyAllWindows()
            # The code is finished
            print("THANK YOU FOR PLAYING!")
            break
        else:
            # Shows an error when Y or N is not the input value
            print("Error: Please enter either 'Y' or 'N'.")
            x = input("Do you want to play or play again? (Y/N): ")
            # fixes spacing accordingly
            if x == "Y" or (str and x != "N"):
                print(" ")

# This is a list that runs the functions in order in the main function
rooms = [room_1, room_2, room_3, item_room, boss_room]

# This runs the main function and causes the code to run
if __name__ == '__main__':
    Main()