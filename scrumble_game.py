import random

# List of words
words = ["python", "computer", "programming", "developer", "keyboard", "flask", "network", "internet"]

print(" Welcome to the Word Scramble Game!")
print("Unscramble the letters to guess the correct word.\n")

# Randomly choose a word
word = random.choice(words)

# Shuffle the word
scrambled = ''.join(random.sample(word, len(word)))

print("Scrambled word:", scrambled)

# Number of tries
tries = 3

while tries > 0:
    guess = input("Your guess: ").lower()

    if guess == word:
        print("\nCorrect! You guessed the word:", word)
        break
    else:
        tries -= 1
        if tries > 0:
            print(f" Wrong!  {tries}\n")
        else:
            print(" Game Over! The correct word was:", word)

"""
output:
 Welcome to the Word Scramble Game!
Unscramble the letters to guess the correct word.

Scrambled word: lrveepdeo
Your guess: developer

Correct! You guessed the word: developer

"""