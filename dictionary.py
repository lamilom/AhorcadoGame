import random

my_file = open("dictionary_words.txt", "r")
data = my_file.read()
dictionary = data.split("\n")
my_file.close()

def random_word():
    azar = random.choice(dictionary)
    return azar.upper()


