import random, string
from copy import copy

vowels = "aeiou"
letters = string.ascii_lowercase
consonants = copy(letters)
for letter in vowels:
    consonants = consonants.replace(letter, "")

prompt = 'What letters do you want? Enter "v" for vowels. "c" for consonants, any other key for any letter (separate letters with a space): '

input_letters = input(prompt)

def pick(l):
    if l == "v":
        return random.choice(vowels)
    elif l == "c":
        return random.choice(consonants)
    else:
        return random.choice(letters)

for i in range(10):
    name = ""
    for letter in input_letters:
        name += pick(letter)
    print(name)
