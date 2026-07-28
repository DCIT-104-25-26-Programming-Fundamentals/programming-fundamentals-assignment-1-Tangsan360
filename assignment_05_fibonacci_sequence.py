# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

fibonacci_sequence = []

def fibonacci() :
    user_input = int(input("Enter a number" ))
    numbers = [x for x in range(user_input)]
    for i in numbers :
        if numbers[i] < numbers[2] :
            fibonacci_sequence.append(numbers[i])
        if numbers[i] >= numbers[2] :
            numbers[i] = numbers[i-1] + numbers[i-2]
            fibonacci_sequence.append(numbers[i])

    for i in fibonacci_sequence :
        print(i,end=" ")

print(fibonacci())

def fibonacci_checker() :
    user_input = int(input("Enter an nth fibonacci number(1 upwards)" ))
    fibonacci_number = int(input("Enter a fibonacci number(0 upwards)" ))
    numbers = [x for x in range(user_input)]
          
    for i in range(user_input) :
        if numbers[i] < numbers[2] :
            fibonacci_sequence.append(numbers[i])
        if numbers[i] >= numbers[2] :
            numbers[i] = numbers[i-1] + numbers[i-2]
            fibonacci_sequence.append(numbers[i])
    if fibonacci_number > user_input :
        if fibonacci_number in fibonacci_sequence :
            print(f"{fibonacci_number} is a fibonacci number")
        else :
            print(f"{fibonacci_number} is NOT a fibonacci number")

    else :
        print(f"{fibonacci_number} must be greater than user_input") 

print(fibonacci_checker())



