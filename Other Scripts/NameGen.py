

import random
import string
import sys


VOWELS = "aeiou"
CONSONANTS = "".join(set(string.ascii_lowercase) - set(VOWELS))


def generate_word(length):
    word = ""
    for i in range(length):
        if i % 2 == 0:
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    
    try:
        count = int(sys.argv[1])
    except:
        count = 1

    for i in range(count):
        return(word)

