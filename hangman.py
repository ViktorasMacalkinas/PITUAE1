import random

def choose_word():
    words = ["codeacademy", "lithuania", "car", "germany", "breaking", "smart", "dog", "sea"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 8
    score = 0

    print("let's beggin!")
    print("Guess the word.")

    while True:
        print("\nAttempts left:", attempts)
        print("Guessed letters:", guessed_letters)
        print(display_word(word, guessed_letters))

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("Nice :) ! but you already guessed that letter.")
            continue

        if guess in word:
            guessed_letters.append(guess)
            if set(word) == set(guessed_letters):
                print("Congratulations! You guessed the word:", word)
                score += attempts * 10
                print("Your score:", score)
                break
        else:
            attempts -= 1
            print("Incorrect guess.")
            print_hangman(attempts)
            if attempts == 0:
                print("Sorry :( but you run out of all attempts. The word was:", word)
                print("Your score:", score)
                break

def print_hangman(attempts):
    stages = [
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                  ---
                """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
          ---
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
          ---
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
          ---
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
          ---
        """
    ]
    print(stages[6 - attempts])

hangman()
