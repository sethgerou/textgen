import random, string
from copy import copy

vowels = "aeiou"
letters = string.ascii_lowercase
consonants = copy(letters)
for letter in vowels:
    consonants = consonants.replace(letter, "")

prompt = 'What letters do you want? Enter "v" for vowels. "c" for consonants, "l" for any letter, or another letter to use that letter. (separate letters with a space): '

quantity = input("How many names do you want? ")
input_letters = input(prompt)

def pick(l):
    if l == "v":
        return random.choice(vowels)
    elif l == "c":
        return random.choice(consonants)
    elif l == "l":
        return random.choice(letters)
    else:
        return l

for i in range(int(quantity)):
    name = ""
    for letter in input_letters:
        name += pick(letter)
    print(name)
