from bcolors import bcolors
import new_game
import os

def lose(word):
    os.system("clear")
    print ("\n \n \n \n \n")
    print (bcolors.RED + bcolors.BOLD + "                     __   __               _                      _ " + bcolors.RESET)
    print (bcolors.RED + bcolors.BOLD + "                     \ \ / /__  _   _     | |    ___  ___  ___   | |" + bcolors.RESET)
    print (bcolors.RED + bcolors.BOLD + "                      \ V / _ \| | | |    | |   / _ \/ __|/ _ \  | |" + bcolors.RESET)
    print (bcolors.RED + bcolors.BOLD + "                       | | (_) | |_| |    | |__| (_) \__ \  __/  |_|" + bcolors.RESET)
    print (bcolors.RED + bcolors.BOLD + "                       |_|\___/ \__,_|    |_____\___/|___/\____  (_) \n" + bcolors.RESET)
    print (bcolors.BOLD + "                            The correct word was " + bcolors.YELLOW + word + bcolors.RESET)
    response = input(bcolors.BOLD + "\n \n \n \n \n \n  Do you wanna play again? (y/n)" + bcolors.YELLOW + word + bcolors.RESET)
    if response == "y":
        new_game.new_game()
    elif response == "n":
        quit()
    else:
        lose(word)