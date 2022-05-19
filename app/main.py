#!/usr/bin/env python3


# def check_is_digit(value):
#     if isinstance(value, (int, float)):
#         return True
#     else:
#         return False

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
    forename = input("Enter your forename: ")
    surname = input("Enter your surname: ")
    age = input("Enter your age: ")
    print(f"Hello {forename} {surname}. You are {age} years old.")

def change_text_colour():
    """
    TO DO
    3. Funktion som ändrar färgen på texten i konsolen (och ändrar tillbaka om
    man använder funktionen igen.
    """
    pass

if __name__ == "__main__":
    # hello_world()
    # input_from_user()
    # change_text_colour()
