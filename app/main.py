#!/usr/bin/env python3
from datetime import datetime
import random
import os

def input_alpha_string(question_text):
    """
    Asks for user input. Checks that the input is an alphabetic string. Returns
    the alphabetic string.

    Parameters:
        question_text (str): A question the user is asked to respond to.

    Returns:
        alpha_string (str): The user's input.
    """

    while True:
        alpha_string = input(question_text).strip()
        if alpha_string.isalpha():
            break
        else:
            print("Error! Please enter an alphabetic string")
            continue

    return alpha_string


def input_integer(question_text):
    """
    Asks for user input. Checks that the input is an integer. Returns the
    integer.

    Parameters:
        question_text (str): A question the user is asked to respond to.

    Returns:
        the_integer (int): The user's input.
    """

    while True:
        try:
            the_integer = int(input(question_text))
            break
        except ValueError:
            print("Error! Please enter an integer")
            continue

    return the_integer


def input_decimal(question_text):
    """
    Asks for user input. Checks that the input is a decimal number. Returns the
    decimal number.

    Parameters:
        question_text (str): A question the user is asked to respond to.

    Returns:
        the_decimal (int): The user's input.
    """

    while True:
        try:
            the_decimal = float(input(question_text))
            break
        except ValueError:
            print("Error! Please enter a decimal number")
            continue

    return the_decimal


def hello_world():
    """
    1. Funktion som skriver ut ”Hello World” i konsolen.
    """

    print("Hello World!")


def input_from_user():
    """
    2. Funktion som tar in input från användaren (Förnamn, Efternamn, Ålder)
    och sedan skriver ut dessa i konsolen.
    """

    forename = input_alpha_string("Enter your forename: ")
    surname = input_alpha_string("Enter your surname: ")
    age = input_integer("Enter your age: ")
    print(f"Hello {forename} {surname}. You are {age} years old.")


def change_text_colour():
    """
    TO DO
    3. Funktion som ändrar färgen på texten i konsolen (och ändrar tillbaka om
    man använder funktionen igen).
    """
    pass


def todays_date():
    """
    4. Funktion för att skriva ut dagens datum.
    """

    todays_date = datetime.now().strftime("%Y-%m-%d")
    print(f"Date: {todays_date}")


def print_largest():
    """
    5. Funktion som tar två input värden, sedan skriver ut vilket av dem som är
    störst.
    """

    integer1 = input_integer("Enter first integer: ")
    integer2 = input_integer("Enter second integer: ")

    if integer1 > integer2:
        largest = integer1
    else:
        largest = integer2

    print(f"Two integers were entered: {integer1} and {integer2}")
    print(f"The largest integer is {largest}")


def number_guesser():
    """
    6. Funktion som genererar att slumpmässigt tal mellan 1 och 100. Användaren
    ska sedan gissa talet. Gissar användaren rätt så ska ett meddelande
    sägadetta, samt hur många försök det tog. Gissar användaren fel ska ett
    meddelande visas som informerar ifall talet var för stort eller för litet.
    """

    random_number = random.randint(1, 100)
    guesses = 0

    print(f"Hint: the random number is {random_number}")

    while True:
        user_guess = input_integer("Guess the number between 1 - 100: ")
        guesses += 1
        if user_guess == random_number:
            break
        else:
            if user_guess < random_number:
                message = "Too low!"
            else:
                message = "Too high!"
            print(f"{message} Try again!")
            continue

    if guesses > 1:
        guess_text = "guesses"
    else:
        guess_text = "guess"

    print(f"Congratulations! It took {guesses} {guess_text} to get the right number!")


def write_text_to_file(text_file):
    """
    7. Funktion där användaren skriver in en textrad, som sedan sparas i en fil
    på hårddisken.

    Parameters:
        text_file (str): Path of the file being written to.
    """

    print("Write a line of text. We're going to save that text to a file.")
    text = input("\n\n> ")
    with open(text_file, "w") as f:
        f.write(text)

    print(f"\nFile saved to {text_file}")


def read_text_from_file(text_file):
    """
    8. Funktion där en fil läses in från hårddisken (för enkelhetens skull kan
    man använda filen från uppgift 7)

    Parameters:
        text_file (str): Path of the file being read from.
    """

    if not os.path.isfile(text_file):
        print("Error! No text file found.")
        write_text_to_file(text_file)

    else:
        pass

    print(f"Reading text from {text_file}\n")
    with open(text_file, "r") as f:
        data = f.read()

    print(f"> {data} <\n")


def decimal_calculations():
    """
    9. Funktion där användaren skickar in ett decimaltal och får tillbakaroten
    ur, upphöjt till 2 och upphöjt till 10.
    """

    decimal = input_decimal("Enter a decimal number: ")
    decimal_square_root = decimal ** (1/2)
    power_of_two = decimal ** 2
    power_of_ten = decimal ** 10

    print(f"Decimal: {decimal}")
    print(f"Square root of {decimal}: {decimal_square_root}")
    print(f"{decimal} raised to the power of 2: {power_of_two}")
    print(f"{decimal} raised to the power of 10: {power_of_ten}")


def decimal_calculations_using_python_modules():
    """
    9. Funktion där användaren skickar in ett decimaltal och får tillbakaroten
    ur, upphöjt till 2 och upphöjt till 10.
    """

    import math

    decimal = input_decimal("Enter a decimal number: ")
    decimal_square_root = math.sqrt(decimal)
    power_of_two = pow(decimal, 2)
    power_of_ten = pow(decimal, 10)

    print(f"Decimal: {decimal}")
    print(f"Square root of {decimal}: {decimal_square_root}")
    print(f"{decimal} raised to the power of 2: {power_of_two}")
    print(f"{decimal} raised to the power of 10: {power_of_ten}")


def multiplication_table():
    """
    10. Funktion där programmet skriver ut en multiplikationstabell från 1 till
    10. En ”tabb”ska läggas in efter varje nummer. Försöka att ställa upp det så
    det blir relativt läsbart.
    """
    for i in range(1, 2):
        for j in range(1, 11):
            print(f"{i} * {j} = {1*j}")


def bubble_sort_integers(integer_list):
    """
    Bubble sorts an integer list into ascending order.

    Parameters:
        integer_list (list): A list of integers.

    Returns:
        integer_list (list): A list of integers.
    """

    n = len(integer_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if integer_list[j] > integer_list[j + 1]:
                integer_list[j], integer_list[j + 1] = integer_list[j + 1], integer_list[j]

    return integer_list


def integer_list_sort():
    """
    11. Funktion som skapar två arrayer. Den första fylls med slumpmässiga tal.
    Den andra fylls med talen från den första i stigande ordning.
    Array.Sort() får EJ användas.
    """

    random_integer_list = [random.randint(1, 100) for i in range(11)]
    random_integer_list_copy = random_integer_list.copy()
    sorted_integer_list = bubble_sort_integers(random_integer_list_copy)

    print(f"Unsorted list:\t{random_integer_list}")
    print(f"Sorted list:\t{sorted_integer_list}")


def palindrome():
    """
    12. Funktion som tar en input från användaren och kontrollerar ifall det är
    en palindrom (alltså samma ord från båda håll, såsom Anna eller radar).
    """

    user_input_raw = input_alpha_string("Enter a word: ")
    user_input_sanitised = user_input_raw.lower()

    if user_input_sanitised == user_input_sanitised[::-1]:
        is_palindrome = True
    else:
        is_palindrome = False

    print(f"{user_input_raw} is a palindrome: {is_palindrome}")


def intervening_integers():
    """
    13. Funktion som tar två inputs från användaren och skriver sedan ut alla
    siffror som är mellan de två inputsen.
    """

    integer1 = input_integer("Enter first integer: ")
    integer2 = input_integer("Enter second integer: ")

    intervening_integer_list = []

    integer1 += 1
    while integer1 < integer2:
        intervening_integer_list.append(integer1)
        integer1 += 1

    print(f"Start integer: {integer1}")
    print(f"Intervening integers: {intervening_integer_list}")
    print(f"End integer: {integer2}")


def convert_user_integer_input_string_to_list(user_input):
    """
    Converts a comma separated integer string into a list of actual integers
    e.g. "1, 2 , 3, 4" -> [1, 2, 3, 4]

    Parameters:
        user_input (str): A string of comma separated integers

    Returns:
        integer_list (int): A list of integers
    """

    split_user_input = user_input.split(",")
    integer_list = [int(i.strip()) for i in split_user_input]

    return integer_list


def sort_user_integer_input_string_into_odd_and_even_integers():
    """
    14. Funktion där användaren skickar in ett antal värden (komma-separerade
    siffror) som sedan sorteras och skrivs ut efter udda och jämna värden.
    """

    while True:
        try:
            user_input = input("Enter a list of comma separated integers: ")
            user_integer_list = convert_user_integer_input_string_to_list(user_input)
            break
        except ValueError:
            print("Invalid data! Please enter comma separated integers e.g. 33, 5, 42, 99, -1746")
            continue

    odd_list = []
    even_list = []

    user_integer_list_copy = user_integer_list.copy()
    sorted_integer_list = bubble_sort_integers(user_integer_list_copy)

    for i in sorted_integer_list:
        if (i % 2) == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    print(f"Orig:\t{user_integer_list}")
    print(f"Sorted:\t{sorted_integer_list}")
    print(f"Even:\t{even_list}")
    print(f"Odd:\t{odd_list}")


def add_user_integer_input_string_together():
    """
    15. Funktion där användaren skriver in ett antal värden(komma-separerade
    siffor) som sedan adderas och skrivs ut.
    """

    while True:
        try:
            user_input = input("Enter a list of comma separated integers: ")
            user_integer_list = convert_user_integer_input_string_to_list(user_input)
            break
        except ValueError:
            print("Invalid data! Please enter comma separated integers e.g. 33, 5, 42, 99, -1746")
            continue

    print(f"Orig:\t{user_integer_list}")
    print(f"Add:\t {sum(user_integer_list)}")


class Character(object):
    """
    A class to represent a character.

    ...

    Attributes
    ----------
    name : str
        first name of the person
    health : int
        the character's health stat
    strength : int
        the character's strength stat
    luck : int
        the character's health luck

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """

    def __init__(self, name, health, strength, luck):
        self.name = name
        self.health = health
        self.strength = strength
        self.luck = luck

    def update_health_score(self, value):
        self.health += value

    def update_strength_score(self, value):
        self.strength += value

    def update_luck_score(self, value):
        self.luck += value


class Hero(Character):
    """docstring for ."""

    def __init__(self, name, health, strength, luck):
        Character.__init__(self, name, health, strength, luck)
        self.character_type = "Hero"


class Villain(Character):
    """docstring for ."""

    def __init__(self, name, health, strength, luck):
        Character.__init__(self, name, health, strength, luck)
        self.character_type = "Villain"


def character_generator():
    """
    16. Funktion där användaren ska ange namnet på sin karaktär och namnet på en
    motståndare. Funktionenskall sedan själv lägga till slumpmässiga värden för
    Hälsa, Styrka och Tur, som sparas i en instans av en klass.
    """

    hero_name = "Andrew"  # input("Please enter the name of the hero: ")
    villain_name = "Werdna"  # input("Please enter the name of the villain")

    player1 = Hero(
        name=hero_name,
        health=random.randint(1, 10),
        strength=random.randint(1, 10),
        luck=random.randint(1, 10)
        )
    player2 = Villain(
        name=villain_name,
        health=random.randint(1, 10),
        strength=random.randint(1, 10),
        luck=random.randint(1, 10)
        )

    player_list = [player1, player2]

    for player in player_list:
        print(f"Name: {player.name}")
        print(f"Type: {player.character_type}")
        print(f"Starting Health: {player.health}")
        print(f"Starting Strength: {player.strength}")
        print(f"Starting Luck: {player.luck}")
        print()


if __name__ == "__main__":

    working_dir = os.path.dirname(os.path.abspath(__file__))
    text_file = os.path.join(working_dir, "text_file.txt")

    # hello_world()  # 1
    # input_from_user()  # 2
    # change_text_colour() # 3 TODO
    # todays_date()  # 4
    # print_largest()  # 5
    # number_guesser()  # 6
    # write_text_to_file(text_file)  # 7
    # read_text_from_file(text_file)  # 8
    # decimal_calculations()  # 9
    # decimal_calculations_using_python_modules()  # 9
    # multiplication_table()  # 10
    # integer_list_sort()  # 11
    # palindrome()  # 12
    # intervening_integers()  # 13
    # sort_user_integer_input_string_into_odd_and_even_integers()  # 14
    # add_user_integer_input_string_together()  # 15
    # character_generator()  # 16
