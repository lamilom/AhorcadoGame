from bcolors import bcolors
import new_game
import os

def win(word):
    os.system("clear")
    print ("\n \n \n \n \n")
    print (bcolors.GREEN + bcolors.BOLD + "                       ____                            _         _       _   _                    _" + bcolors.RESET)
    print (bcolors.GREEN + bcolors.BOLD + "                      / ___|___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  ___   | |" + bcolors.RESET)
    print (bcolors.GREEN + bcolors.BOLD + "                     | |   / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|  | |" + bcolors.RESET)
    print (bcolors.GREEN + bcolors.BOLD + "                     | |__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \  |_|" + bcolors.RESET)
    print (bcolors.GREEN + bcolors.BOLD + "                      \____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/  (_)" + bcolors.RESET)
    print (bcolors.GREEN + bcolors.BOLD + "                                       |___/                                                     " + bcolors.RESET)
    print (bcolors.BOLD + "\n \n                                      The correct word was " + bcolors.YELLOW + word + bcolors.RESET)
    response = input(bcolors.BOLD + "\n \n \n \n \n \n  Do you wanna play again? (y/n)" + bcolors.RESET)
    if response == "y":
        new_game.new_game()
    elif response == "n":
        quit()
    else:
        win(word)