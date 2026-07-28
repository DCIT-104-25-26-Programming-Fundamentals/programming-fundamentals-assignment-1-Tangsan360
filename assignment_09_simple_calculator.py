# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

import sys
options = ["Addtion","Subtraction","Multiplication","Division","Modulus","Exponent","Quit"]
for position,option in enumerate(options) :
    print(f"{position} : {option}")
user_input = int(input("enter an arithmetic option"))
def addtion(a,b):
    print(a+b)

def subtraction(a,b):
    print9(a-b)

def Multiplication(a,b):
    print(a*b)

def Division(a,b):
    result = a/b
    print(f"{result:.2f}")
    try :
        a/b
    except ZeroDivisionError :
        print("cannot divide by zero")

def Modulus(a,b):
    print(a%b)

def Exponentiation(a,b):
    print(a**b)

def Quit():
    sys.exit()


def calculator() :
    
    while 1<=user_input<=7 :
         
        if user_input == 1 :
            print(addtion())
        elif user_input == 2 :
            print(subtraction())
        elif user_input == 3 :
            print(Multiplication())
        elif user_input == 4 :
            print( Division())
        elif user_input == 5 :
            print(Modulus)
        elif user_input == 6 :
            print(Exponentiation())
        elif user_input == 7 :
            print(Quit())
        else :
            print("option is out of range")
        user_input = int(input("enter an arithmetic option"))


    print(calculator())