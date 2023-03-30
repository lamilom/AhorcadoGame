import select_word
from bcolors import bcolors

test = 0
counter = 10
used = []
print (used)
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
    else:
        busqueda(character)
    used.append(character)
    if test == 0:
        counter -= 1
    test = 0
    if counter == 0:
        break
if discovered == hint:
    print (bcolors.GREEN + bcolors.BOLD + "        ____                            _         _       _   _                    _" + bcolors.RESET)
    print (bcolors.GREEN + bcolors.BOLD + "       / ___|___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  ___   | |" + bcolors.RESET)
    print (bcolors.GREEN + bcolors.BOLD + "      | |   / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|  | |" + bcolors.RESET)
    print (bcolors.GREEN + bcolors.BOLD + "      | |__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \  |_|" + bcolors.RESET)
    print (bcolors.GREEN + bcolors.BOLD + "       \____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/  (_)" + bcolors.RESET)
    print (bcolors.GREEN + bcolors.BOLD + "                        |___/                                                     " + bcolors.RESET)
else:
    print (bcolors.RED + bcolors.BOLD + " __   __               _                      _ " + bcolors.RESET)
    print (bcolors.RED + bcolors.BOLD + " \ \ / /__  _   _     | |    ___  ___  ___   | |" + bcolors.RESET)
    print (bcolors.RED + bcolors.BOLD + "  \ V / _ \| | | |    | |   / _ \/ __|/ _ \  | |" + bcolors.RESET)
    print (bcolors.RED + bcolors.BOLD + "   | | (_) | |_| |    | |__| (_) \__ \  __/  |_|" + bcolors.RESET)
    print (bcolors.RED + bcolors.BOLD + "   |_|\___/ \__,_|    |_____\___/|___/\____  (_) \n" + bcolors.RESET)

    print (bcolors.BOLD + "      The correct word was " + bcolors.YELLOW + select_word.selected_word + bcolors.RESET)