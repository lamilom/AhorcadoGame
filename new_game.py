import select_word
from bcolors import bcolors
import win
import lose
import os

test = 0


def new_game():
    used = []
    counter = 5
    os.system("clear")
    select_word.new_word()
    hint = [*select_word.selected_word]
    discovered = []
    discovered.append(select_word.first_character)
    used.append(select_word.first_character)
    for letter in select_word.selected_word:
        discovered.append('_')
    discovered.pop()
    discovered_str = " ".join(str(x) for x in discovered)
    print (f"{bcolors.BOLD}    {discovered_str} \n \n {bcolors.RESET}")

    for i in range(len(hint)):
            if select_word.first_character == hint[i]:
                discovered[i] = hint[i]
    def busqueda(character):
        for i in range(len(hint)):
            if character == hint[i]:
                global test
                discovered[i] = hint[i]
                test = 1
        discovered_str = " ".join(str(x) for x in discovered)
        print (f"{bcolors.BOLD}    {discovered_str} \n \n {bcolors.RESET}")
    while discovered != hint:
        global test
        if counter >= 7:
            print(bcolors.GREEN + "You have " + str(counter) + " attempts" + bcolors.RESET)
        if counter >= 4 and counter < 7:
            print(bcolors.YELLOW + "You have " + str(counter) + " attempts" + bcolors.RESET)
        if counter <= 3:
            print(bcolors.RED + "You have " + str(counter) + " attempts" + bcolors.RESET)
        character = input("Insert a character:").upper()
        if character in used:
            print(f"The {character} has been used, please try again")
            test = 1
        elif character == select_word.selected_word:
            discovered = hint
            break
        else:
            busqueda(character)
        used.append(character)
        if test == 0:
            counter -= 1
        test = 0
        if counter <= 0:
            break
    if discovered == hint:
        win.win(select_word.selected_word)
        
    else:
       lose.lose(select_word.selected_word)
       