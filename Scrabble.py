import random

# define the letter scores
scores = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1,
    "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1,
    "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
}

def generate_letters():
    """
    Generates a list of six letters, randomly chosen from the alphabet.
    """
    letters = [random.choice(list(scores.keys())) for _ in range(6)]
    return letters

def calculate_score(word):
    """
    Calculates the Scrabble score for a given word.
    """
    score = sum([scores[letter.upper()] for letter in word])
    return score

def main():
    play_again = True
    while play_again:
        letters = generate_letters()
        print("Generated letters:", " ".join(letters))
        satisfied = input("Are you satisfied with these letters? (Y/N) ")
        if satisfied.upper() == "N":
            continue
        done = False
        while not done:
            word = input("Enter a word using these letters: ")
            if len(word) < 2:
                print("Words must be at least two letters long.")
            elif any(letter.upper() not in letters for letter in word):
                print("You can't use letters that weren't generated.")
            else:
                for letter in set(word):
                    if word.count(letter) > letters.count(letter.upper()):
                        print(f"You can't use {word}, because it uses more {letter.upper()} than were generated.")
                        break
                else:
                    score = calculate_score(word)
                    print(f"Your word '{word}' has a score of {score} points.")
                    done = True
        again = input("Do you want to play again? (Y/N) ")
        play_again = again.upper() == "Y"

if __name__ == "__main__":
    main()
