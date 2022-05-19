#!/usr/bin/env python3
from datetime import datetime
import random
import os

# def check_is_digit(value):
#     if isinstance(value, (int, float)):
#         return True
#     else:
#         return False


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
        alpha_string = input(question_text)
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
            print("Try again!")
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
    for i in range(1,2):
        for j in range(1, 11):
            print(f"{i} * {j} = {1*j}")

def list_sort():
    """
    11. Funktion som skapar två arrayer. Den första fylls med slumpmässiga tal.
    Den andra fylls med talen från den första i stigande ordning.
    Array.Sort() får EJ användas.
    """

    list_to_be_sorted = [random.randint(1, 100) for i in range(11)]
    print(f"Unsorted list:\t{list_to_be_sorted}")

    # Bubble
    n = len(list_to_be_sorted)
    for i in range(n):
        for j in range(0, n-i-1):
            if list_to_be_sorted[j] > list_to_be_sorted[j + 1]:
                list_to_be_sorted[j], list_to_be_sorted[j + 1] = list_to_be_sorted[j + 1], list_to_be_sorted[j]

    print(f"Sorted list:\t{list_to_be_sorted}")

if __name__ == "__main__":
    working_dir = os.path.dirname(os.path.abspath(__file__))
    text_file = os.path.join(working_dir, "text_file.txt")

    # hello_world()
    # input_from_user()
    # change_text_colour() # TODO
    # todays_date()
    # print_largest()
    # number_guesser()
    # write_text_to_file(text_file)
    # read_text_from_file(text_file)
    # decimal_calculations()
    # decimal_calculations_using_python_modules()
    # multiplication_table()
    list_sort()
