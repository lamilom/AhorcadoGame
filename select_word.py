from dictionary import random_word
from bcolors import bcolors
#Before start we need to select a random word // Antes de empezar necesitamos seleccionar una palabra al azar

selected_word = random_word()
large = len(selected_word)
word_characters = [*selected_word]
first_character = str(word_characters[0])
def new_word():
    print (f"{bcolors.BLUE}\n {bcolors.BOLD}\n The word has {large} characters and starts with {first_character} \n {bcolors.RESET} \n")
#    print (f"The word is {selected_word}")
    return