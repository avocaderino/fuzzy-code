"""A game of hangman"""
import random
import string
from words import words


def usable_word(length):
    """Returns a word from words.py without any special characters"""
    word = random.choice(words)
    while "-" in word or " " in word or len(word) != length:
        # keeps choosing a random word untill a valid word is obtained
        word = random.choice(words)

    return word.upper()


def hangman(lives=7):
    """Initializes a game of hangman against the computer"""
    num = int(input("What word length do you want?\n"))
    word = usable_word(num)
    actual_letters = list(word)
    used_letters = letters_in_word = []
    available_letters = list(string.ascii_uppercase)
    unguessed_letters = num

    # printing the word
    while lives > 0 and unguessed_letters != 0:
        for dash in word:
            if dash not in letters_in_word:
                print("_ ", end="")
            elif dash in letters_in_word:
                print(dash, end=" ")
        num_letters = 0
        # playing the game
        guessed_letter = input(
            f"\n{unguessed_letters} more letter(s) to go and you "
            f"have {lives} lives/life left. Press a letter\n").upper()

        if (guessed_letter not in used_letters and
                guessed_letter in available_letters):
            # checking how many times the letter occurs in the word
            while guessed_letter in actual_letters:
                num_letters += 1
                break
            # the letter is not in the word
            if num_letters == 0:
                print("The letter is not present in the word.")
                lives -= 1
            else:
                # the letter is in the word
                print(f"The letter is present {num_letters} "
                      "times in the word")
                unguessed_letters -= num_letters
                letters_in_word.append(guessed_letter)
            used_letters.append(guessed_letter)
            available_letters.remove(guessed_letter)
        # the letter has already been guessed before
        elif guessed_letter in used_letters:
            print(
                "You have already guessed this letter once. "
                "Please choose another letter")
        # input is not a letter
        elif guessed_letter not in used_letters or available_letters:
            print("Letters only please")

    # ran out of tries
    if lives == 0:
        print(f"You have run out of lives.I win. The word was {word}")
    # player win
    else:
        print(
            f"You have defeated me with {lives} lives remaining. Enjoy this "
            f"victory while it lasts. I will be back.\nThe word was {word}")


hangman()
