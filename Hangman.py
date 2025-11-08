import random

# List of possible words
words = ["python", "computer", "programming", "developer", "hangman", "keyboard", "flask", "network"]

# Randomly choose a word
word = random.choice(words)
guessed_letters = []
tries = 6

# Automatically reveal first and last letters
guessed_letters.append(word[0])
guessed_letters.append(word[-1])

print(" Welcome to Hangman Game!")
print("Guess the word before you run out of chances!")


# Game loop
while tries > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print(f"Remaining tries: {tries}")

    # Check if user has guessed the word
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        tries -= 1
        print(" Wrong guess!\n")
    else:
        print("Good guess!\n")

# If the player runs out of tries
if tries == 0:
    print(" Game Over! The word was:", word)

"""
output:

 Welcome to Hangman Game!
Guess the word before you run out of chances!
Word: c _ _ _ _ _ _ r 
Remaining tries: 6
Enter a letter: u
Good guess!

Word: c _ _ _ u _ _ r 
Remaining tries: 6
Enter a letter: i
 Wrong guess!

Word: c _ _ _ u _ _ r 
Remaining tries: 5
Enter a letter: y
 Wrong guess!

Word: c _ _ _ u _ _ r 
Remaining tries: 4
Enter a letter: o
Good guess!

Word: c o _ _ u _ _ r 
Remaining tries: 4
Enter a letter: m
Good guess!

Word: c o m _ u _ _ r 
Remaining tries: 4
Enter a letter: p
Good guess!

Word: c o m p u _ _ r 
Remaining tries: 4
Enter a letter: u
You already guessed that letter.

Word: c o m p u _ _ r 
Remaining tries: 4
Enter a letter: t
Good guess!

Word: c o m p u t _ r 
Remaining tries: 4
Enter a letter: l
 Wrong guess!

Word: c o m p u t _ r 
Remaining tries: 3
Enter a letter: e
Good guess!

Word: c o m p u t e r 
Remaining tries: 3

Congratulations! You guessed the word: computer

Process finished with exit code 0





"""