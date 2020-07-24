import random
import string
from Hangman_state import State

Main_word = ""
Life = 6
Guessed_letters = set()


def readfile(filename):
    """
    Read the txt file and return it as a list
    :param filename: Name of the txt file which contains words
    :return: return a list of all the words
    """
    with open(filename, "r") as file:
        lines = file.read().splitlines()
        return lines


def valid_word(word):
    """
    Check if the chosen word is valid or not.
    The word should not contain spacing or dash
    Both conditions must be met to return a True
    :param word: The random word
    :return: Boolean True or False
    """
    return " " not in word and "-" not in word


def random_word():
    """
    Find a random word from a list provided by readfile()
    Using the choice module which gives a single "random" element from a sequence
    :return: Random word
    """
    Word = random.choice(readfile("words.txt"))
    while not valid_word(Word):
        Word = random.choice(readfile("words.txt"))
    return Word


def print_guessed():
    """
    Prints out the guessed words
    :return:
    """
    print("Used letters: ", " , ".join(Guessed_letters))


def print_word():
    """
    Prints the underscores matching the number of letters, when the user gives the right letter
    it will replace the underscore with the letter
    :return:
    """
    for i in Main_word:
        if i in Guessed_letters:
            print(i, end="")
        else:
            print(" _ ", end="")


def guessed_letter(letter):
    """
    Adds the letter to the global set "Guessed_letters"
    :param letter: Letter provided from the user
    :return:
    """
    Guessed_letters.add(letter)


def valid_letters(letter):
    """
    Alphabet is a list with the english alphabet imported from the string module.
    Checking if the letter is in the list Alphabet.
    :param letter: The letter the user provided
    :return: Boolean True or False
    """
    Alphabet = list(string.ascii_lowercase)
    return letter in Alphabet


def correct_guess(letter):
    """
    Check if the letter is correct
    :param letter: letter provided by the user
    :return: boolean
    """
    return letter in set(Main_word)


def won_game():
    """
    You won the game if you guessed all the right letters
    Checks if the main word is a subset of the guessed words
    :return: Boolean
    """
    return set(Main_word).issubset(Guessed_letters)


def lost_game():
    """
    You loose the game if you run out of chances
    :return: Boolean
    """
    return Life == 0


def game_over():
    """
    Checks if the game is over
    :return: Boolean
    """
    return won_game() or lost_game()


def user_input():
    """
    Ask the user to provide a letter
    Checks if the letter is valid
    :return: The letter the user provided
    """
    letter = input("Guess a letter a-z ").lower()
    while not valid_letters(letter):
        print()
        print("{} is not a valid letter ".format(letter))
        letter = user_input()
    return letter


def game_hangman():
    """
    The main function that combine all the other functions
    :return:
    """
    global Main_word
    global Life
    print("------- HANGMAN -------")
    Main_word = random_word().lower()
    print(Main_word)
    while not game_over():
        print(State[Life])
        print_word()
        print()
        print_guessed()
        letter = user_input()
        guessed_letter(letter)
        if not correct_guess(letter):
            Life -= 1
        if game_over():
            print("The game is over")
            if won_game():
                print(State[Life])
                print("You won the game, {} is the word" .format(Main_word))
            elif lost_game():
                print(State[Life])
                print("You lost the game, {} was the word".format(Main_word))


def main():
    game_hangman()


main()
