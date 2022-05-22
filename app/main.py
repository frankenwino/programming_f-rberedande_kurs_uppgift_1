#!/usr/bin/env python3
import os
import random
import sys
from datetime import datetime

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
    clear_screen()
    print(f"{hello_world.__doc__.strip()}\n")

    print("Hello World!")

    return_to_menu()


def input_from_user():
    """
    2. Funktion som tar in input från användaren (Förnamn, Efternamn, Ålder)
    och sedan skriver ut dessa i konsolen.
    """
    clear_screen()
    print(f"{input_from_user.__doc__.strip()}\n")

    forename = input_alpha_string("Enter your forename: ")
    surname = input_alpha_string("Enter your surname: ")
    age = input_integer("Enter your age: ")
    print(f"Hello {forename} {surname}. You are {age} years old.")

    return_to_menu()


def change_text_colour():
    """
    3. Funktion som ändrar färgen på texten i konsolen (och ändrar tillbaka om
    man använder funktionen igen).

    Credit: https://gist.github.com/Prakasaka/219fe5695beeb4d6311583e79933a009
    """

    clear_screen()
    print(f"{change_text_colour.__doc__.strip()}\n")

    # print(ansi_code_list[0])

    print(f"{ansi_code_list[0]}Colour change!")
    ansi_code_list.reverse()
    # print(ansi_code_list[0])

    return_to_menu()


def todays_date():
    """
    4. Funktion för att skriva ut dagens datum.
    """

    clear_screen()
    print(f"{todays_date.__doc__.strip()}\n")

    the_date = datetime.now().strftime("%Y-%m-%d")
    print(f"Date: {the_date}")

    return_to_menu()


def print_largest():
    """
    5. Funktion som tar två input värden, sedan skriver ut vilket av dem som är
    störst.
    """

    clear_screen()
    print(f"{print_largest.__doc__.strip()}\n")

    integer1 = input_integer("Enter first integer: ")
    integer2 = input_integer("Enter second integer: ")

    if integer1 == integer2:
        largest = None
    elif integer1 > integer2:
        largest = integer1
    else:
        largest = integer2

    print(f"Two integers were entered: {integer1} and {integer2}")

    if largest is None:
        print(f"The integers are the same.")
    else:
        print(f"The largest integer is {largest}")

    return_to_menu()


def number_guesser():
    """
    6. Funktion som genererar att slumpmässigt tal mellan 1 och 100. Användaren
    ska sedan gissa talet. Gissar användaren rätt så ska ett meddelande
    sägadetta, samt hur många försök det tog. Gissar användaren fel ska ett
    meddelande visas som informerar ifall talet var för stort eller för litet.
    """

    clear_screen()
    print(f"{number_guesser.__doc__.strip()}\n")

    random_number = random.randint(1, 100)
    guesses = 0

    print(f"Hint: the random number is {random_number}\n")

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

    print(f"\nCongratulations! It took {guesses} {guess_text} to get the right number!")

    return_to_menu()


def write_text_to_file(text_file):
    """
    7. Funktion där användaren skriver in en textrad, som sedan sparas i en fil
    på hårddisken.

    Parameters:
        text_file (str): Path of the file being written to.
    """

    clear_screen()
    print(f"{write_text_to_file.__doc__.strip()}\n")

    print("Write a line of text. We're going to save that text to a file.")
    text = input("\n\n> ")
    with open(text_file, "w") as f:
        f.write(text)
    print(f"\nFile saved to {text_file}")

    return_to_menu()


def read_text_from_file(text_file):
    """
    8. Funktion där en fil läses in från hårddisken (för enkelhetens skull kan
    man använda filen från uppgift 7)

    Parameters:
        text_file (str): Path of the file being read from.
    """

    clear_screen()
    print(f"{read_text_from_file.__doc__.strip()}\n")

    if not os.path.isfile(text_file):
        print("Error! No text file found.")
        write_text_to_file(text_file)

    else:
        pass

    print(f"Reading text from {text_file}\n")
    with open(text_file, "r") as f:
        data = f.read()

    print(f"> {data} <\n")

    return_to_menu()


def decimal_calculations():
    """
    9. Funktion där användaren skickar in ett decimaltal och får tillbakaroten
    ur, upphöjt till 2 och upphöjt till 10.
    """

    clear_screen()
    print(f"{decimal_calculations.__doc__.strip()}\n")

    decimal = input_decimal("Enter a decimal number: ")
    decimal_square_root = decimal ** (1/2)
    power_of_two = decimal ** 2
    power_of_ten = decimal ** 10

    # print(f"Decimal: {decimal}")
    print(f"Square root of {decimal}: {decimal_square_root}")
    print(f"{decimal} raised to the power of 2: {power_of_two}")
    print(f"{decimal} raised to the power of 10: {power_of_ten}")

    return_to_menu()


def decimal_calculations_using_python_modules():
    """
    9. Funktion där användaren skickar in ett decimaltal och får tillbakaroten
    ur, upphöjt till 2 och upphöjt till 10.
    """

    clear_screen()
    print(f"{decimal_calculations_using_python_modules.__doc__.strip()}\n")

    import math

    decimal = input_decimal("Enter a decimal number: ")
    decimal_square_root = math.sqrt(decimal)
    power_of_two = pow(decimal, 2)
    power_of_ten = pow(decimal, 10)

    print(f"Decimal: {decimal}")
    print(f"Square root of {decimal}: {decimal_square_root}")
    print(f"{decimal} raised to the power of 2: {power_of_two}")
    print(f"{decimal} raised to the power of 10: {power_of_ten}")

    return_to_menu()


def multiplication_table():
    """
    10. Funktion där programmet skriver ut en multiplikationstabell från 1 till
    10. En ”tabb”ska läggas in efter varje nummer. Försöka att ställa upp det så
    det blir relativt läsbart.
    """

    clear_screen()
    print(f"{multiplication_table.__doc__.strip()}\n")

    for i in range(1, 2):
        for j in range(1, 11):
            print(f"{i} * {j} = {1*j}")

    return_to_menu()


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

    clear_screen()
    print(f"{integer_list_sort.__doc__.strip()}\n")

    random_integer_list = [random.randint(-100, 100) for i in range(11)]
    random_integer_list_copy = random_integer_list.copy()
    sorted_integer_list = bubble_sort_integers(random_integer_list_copy)

    print(f"Random unsorted integer list:\t{random_integer_list}")
    print(f"Sorted integer list:\t\t{sorted_integer_list}")

    return_to_menu()


def palindrome():
    """
    12. Funktion som tar en input från användaren och kontrollerar ifall det är
    en palindrom (alltså samma ord från båda håll, såsom Anna eller radar).
    """

    clear_screen()
    print(f"{palindrome.__doc__.strip()}\n")

    user_input_raw = input_alpha_string("Enter a word: ")
    user_input_sanitised = user_input_raw.lower()

    if user_input_sanitised == user_input_sanitised[::-1]:
        is_palindrome = True
    else:
        is_palindrome = False

    print(f"{user_input_raw} is a palindrome: {is_palindrome}")

    return_to_menu()


def intervening_integers():
    """
    13. Funktion som tar två inputs från användaren och skriver sedan ut alla
    siffror som är mellan de två inputsen.
    """

    clear_screen()
    print(f"{intervening_integers.__doc__.strip()}\n")


    integer1 = input_integer("Enter first integer: ")
    integer2 = input_integer("Enter second integer: ")
    intervening_integer_list = []

    print(f"Start integer: {integer1}")

    if integer1 < integer2:
        integer1 += 1
        while integer1 < integer2:
            intervening_integer_list.append(str(integer1))
            integer1 += 1
    else:
        integer1 -= 1
        while integer1 > integer2:
            intervening_integer_list.append(str(integer1))
            integer1 -= 1

    print(f"Intervening integers: {', '.join(intervening_integer_list)}")
    print(f"End integer: {integer2}")

    return_to_menu()


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


def sort_user_integer_input_into_odd_and_even_integers():
    """
    14. Funktion där användaren skickar in ett antal värden (komma-separerade
    siffror) som sedan sorteras och skrivs ut efter udda och jämna värden.
    """

    clear_screen()
    print(f"{sort_user_integer_input_into_odd_and_even_integers.__doc__.strip()}\n")

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

    print(f"User's integer list:\t{user_integer_list}")
    print(f"Sorted integers:\t{sorted_integer_list}")
    print(f"Even integers:\t\t{even_list}")
    print(f"Odd integers:\t\t{odd_list}")

    return_to_menu()


def add_user_integer_input_together():
    """
    15. Funktion där användaren skriver in ett antal värden(komma-separerade
    siffor) som sedan adderas och skrivs ut.
    """

    clear_screen()
    print(f"{add_user_integer_input_together.__doc__.strip()}\n")

    while True:
        try:
            user_input = input("Enter a list of comma separated integers: ")
            user_integer_list = convert_user_integer_input_string_to_list(user_input)
            break
        except ValueError:
            print("Invalid data! Please enter comma separated integers e.g. 33, 5, 42, 99, -1746")
            continue

    print(f"User's integer list:\t{user_integer_list}")
    print(f"Sum of integers:\t {sum(user_integer_list)}")

    return_to_menu()


class Character(object):
    """
    A class to represent a character.

    Attributes
    ----------
    name : str
        first name of the person
    health : int
        the character's health stat
    strength : int
        the character's strength stat
    luck : int
        the character's luck

    Methods
    -------
    update_health_score(value):
        Updates the character's health score
    update_strength_score(value):
        Updates the character's strength score.
    update_luck_score(value):
        Updates the character's luck score.
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
    """A Character subclass that represents a Hero character"""

    def __init__(self, name, health, strength, luck):
        Character.__init__(self, name, health, strength, luck)
        self.character_type = "Hero"


class Villain(Character):
    """A Character subclass that represents a Villain character"""

    def __init__(self, name, health, strength, luck):
        Character.__init__(self, name, health, strength, luck)
        self.character_type = "Villain"


def character_generator():
    """
    16. Funktion där användaren ska ange namnet på sin karaktär och namnet på en
    motståndare. Funktionenskall sedan själv lägga till slumpmässiga värden för
    Hälsa, Styrka och Tur, som sparas i en instans av en klass.
    """

    clear_screen()
    print(f"{character_generator.__doc__.strip()}\n")

    hero_name = input("Please enter the name of the hero:\t")
    villain_name = input("Please enter the name of the villain:\t")

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
        print(f"\nName: {player.name}")
        print(f"Type: {player.character_type}")
        print(f"Health: {player.health}")
        print(f"Strength: {player.strength}")
        print(f"Luck: {player.luck}")

    return_to_menu()


def return_to_menu():
    input("\nPress Enter to return to the menu. ")


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_menu():
    clear_screen()
    for key in menu_options.keys():
        print (f'{key}.\t', menu_options[key] )

def exit():
    print("Exiting. Bye!")
    sys.exit(0)


# Variables for write_text_to_file() and read_text_from_file()
working_dir = os.path.dirname(os.path.abspath(__file__))
text_file = os.path.join(working_dir, "text_file.txt")

#  Variables for change_text_colour()
red_text_ansi_code = "\033[31m"
reset_text_colour_ansi_code = "\033[0m"
ansi_code_list = [red_text_ansi_code, reset_text_colour_ansi_code]

# Menu variables
valid_menu_options = [x for x in range(0,17)]
menu_options = {
    1: 'hello_world()',
    2: 'input_from_user()',
    3: 'change_text_colour()',
    4: 'todays_date()',
    5: 'print_largest()',
    6: 'number_guesser()',
    7: 'write_text_to_file(text_file)',
    8: 'read_text_from_file(text_file)',
    9: 'decimal_calculations()',
    10: 'multiplication_table()',
    11: 'integer_list_sort()',
    12: 'palindrome()',
    13: 'intervening_integers()',
    14: 'sort_user_integer_input_into_odd_and_even_integers()',
    15: 'add_user_integer_input_together()',
    16: 'character_generator()',
    0: 'Exit',
}

if __name__ == "__main__":
    menu_error_message = "Error! Please enter a value between 0-16. Press Enter to continue. "
    while True:
        try:
            print_menu()
            option = int(input('\nEnter your choice [0-16]: '))
            if option in valid_menu_options:
                if option == 1:
                    hello_world()
                elif option == 2:
                    input_from_user()
                elif option == 3:
                    change_text_colour()
                elif option == 4:
                    todays_date()
                elif option == 5:
                    print_largest()
                elif option == 6:
                    number_guesser()
                elif option == 7:
                    write_text_to_file(text_file)
                elif option == 8:
                    read_text_from_file(text_file)
                elif option == 9:
                    decimal_calculations()
                elif option == 10:
                    multiplication_table()
                elif option == 11:
                    integer_list_sort()
                elif option == 12:
                    palindrome()
                elif option == 13:
                    intervening_integers()
                elif option == 14:
                    sort_user_integer_input_into_odd_and_even_integers()
                elif option == 15:
                    add_user_integer_input_together()
                elif option == 16:
                    character_generator()
                elif option == 0:
                    exit()
                else:
                    continue
            else:
                input(menu_error_message)
                continue
        except ValueError:
            input(menu_error_message)
            continue
