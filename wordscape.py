import enchant
from itertools import permutations

# Create an instance of the enchant dictionary
d = enchant.Dict("en_US")

letters = input("Enter some letters: ")
words_dict = {3: set(), 4: set(), 5: set(), 6: set()} # number of words need to generate 

# generate words 3, 4, 5, 6, letters
for length in range(3, 7):
    for combination in permutations(letters, length):
        word = ''.join(combination)
        if d.check(word):
            words_dict[length].add(word)

# print the words by their length
for length, words_set in words_dict.items():
    print(f"Words formed from the {length} letters:", ', '.join(words_set))
