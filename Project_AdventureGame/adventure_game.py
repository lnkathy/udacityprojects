# Project: Adventure Game 
import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, please make your choice.")
    return response


def intro(weapon, character):
    print_pause("\nADVENTURE GAME \n")
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + character + " is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.\n")


def field(weapon, character):
    # Things that happen when the player runs back to the field
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?.")
    while True:
        choice1 = valid_input("(Please enter 1 or 2.)\n", "1", "2")
        if choice1 == '1':
            house(weapon, character)
            break
        elif choice1 == '2':
            cave(weapon, character)
            break


def cave(weapon, character):
    # Things that happen to the player goes in the cave
    if "sword" in weapon:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword "
                    "with you.")
        weapon.append("sword")
        print_pause("You walk back out to the field.\n")
    field(weapon, character)


def fight(weapon, character):
    # Things that happen when the player fights
    while True:
        choice2 = valid_input("Would you like to (1) fight or (2) run away?\n",
                              "1", "2")
        if choice2 == '1':
            if "sword" in weapon:
                print_pause("As the " + character + " moves to attack, you "
                            "unsheathe your new sword.")
                print_pause("The Sword of Ogoroth shines brightly in your "
                            "hand as you brace yourself for the attack.")
                print_pause("But the " + character + " takes one look at "
                            "your shiny new toy and runs away!")
                print_pause("You have rid the town of the " + character +
                            ". You are victorious!\n")
            else:
                print_pause("You do your best...")
                print_pause("but your dagger is no match for the "
                            + character + ".")
                print_pause("You have been defeated!")
            play_again()
            break
        elif choice2 == '2':
            print_pause("\nYou run back into the field. Luckily, you don't "
                        "seem to have been followed.\n")
            field(weapon, character)
            break


def house(weapon, character):
    # Things that happen to the player in the house
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a "
                + character + ".")
    print_pause("Eep! This is the " + character + "'s house!")
    print_pause("The " + character + " attacks you!")
    print_pause("You feel a bit under-prepared for this, what with only having"
                " a tiny dagger.")
    fight(weapon, character)


def play_game():
    weapon = []
    character = random.choice(["wicked fairie", "pirate", "dragon", "troll",
                               "orc", "gorgon"])
    intro(weapon, character)
    field(weapon, character)


def play_again():
    print_pause("\nGAME OVER \n")
    response = valid_input("Would you like to play again? (y/n) ", "y", "n")
    if "y" in response:
        print_pause("\nExcellent! Restarting the game ... ")
        play_game()
    elif "n" in response:
        print_pause("\nThanks for playing! See you next time.")
        exit(0)
    play_again()


play_game()
