# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
import sys
 
student_data = [ ]
user_input = int(input("Enter your choice"))

def identity_generator() :
    student_name = input("Enter your name")
    number_of_scores = int(input("How many scores?"))
    student_scores =[ ]
    for i in range(number_of_scores) :
        score = int(input("Enter your score"))
        student_scores.append(score)
    student_id = input("Enter your id")
    result = [("name",student_name),("scores",student_scores),("id",student_id)]
    final = dict(result)
    student_data.append(final)

def formatted_table() :
    print(f"{'id':<10} | {'name':<15} | {'scores'}") 
    print("-"*40)
    for student in student_data :
        scores_str = ",".join(map(str,student["scores"]))
        print(f"{student["id"]:<10} | {student["name"]:<15} | {scores_str}") 

def mean_score() :
    id_checker = input("Enter your id")

    for student in student_data :
        if id_checker in student["id"] :
            print(f"student name is {student["name"]}")
            total_score = sum(scores["score"])
            average = total_score/len(scores[score])
            print(average)
        else :
            print("id NOT found")

def done():
    sys.exit("Bye Bye")


def student_records() :

    if user_input ==1 :
        print(identity_generator())

    elif user_input == 2 :
        print(formatted_table())
    
    elif user_input == 3 :
        print(mean_score())

    elif user_input == 4 :
        print(done())
    
    else :
        print(f"{user_input} is out of option range")

print(identity_generator())
print(formatted_table())