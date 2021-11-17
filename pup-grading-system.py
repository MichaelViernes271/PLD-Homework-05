"""
Topic: Programming Logic and Desin
Author: Viernes, Michael
College: BSCOE 1-1
Submitted to: Mr. Danilo Madrigalejos
"""

from sys import exit
import math as m # Might be useful at some point.

def inputGrade(): # Asks number of grade.
    grade = input("Please enter the requested grade: ")
    return grade

def equateGrade(grade): # Returns equivalent CLASS MARK and DESCRIPTION.

    grade_dict = getGradingDict()
    if grade.isdigit():
        grade = int(grade)
        if grade >= 97 and grade <= 100:
            return str("1.00: Excellent")
        elif grade >= 94:
            return str("1.25: Excellent")
        elif grade >= 91:
            return str("1.50: Very Good")
        elif grade >= 88:
            return str("1.75: Very Good")
        elif grade >= 85:
            return str("2.00: Good")
        elif grade >= 82:
            return str("2.25: Good")
        elif grade >= 79:
            return str("2.50: Satisfactory")
        elif grade >= 76:
            return str("2.75: Satisfactory")
        elif grade == 75:
            return str("3.00: Passing")
        elif grade >= 65:
            return str("5.00: Failure")
        else:
            print("Input error.")
    if grade.isalpha():
        grade = grade.lower()
        if grade == 'inc':
            return str("Inc: Incomplete") 
        elif grade == 'w':
            return str("W: Withdrawn")
        elif grade == 'd':
            return str("D: Dropped")
        else:
            # raise Exception("\n\n\nThe input is under or beyond the limit!\n\n")
            print("Input error")
            exit()

def getGradingDict(): # Creates a dictionary of grades where: keys = class mark, values = description.
    gradeMark = {
        1.00: "Excellent", 1.25: "Excellent",
        1.50: "Very Good", 1.75: "Very Good",
        2.00: "Good", 2.25: "Good", 
        2.50: "Satisfactory", 2.75: "Satisfactory",
        3.00: "Passing", 5.00: "Failure", 
        "Inc": "Incomplete", "W": "Withdrawn", "D": "Dropped"
    }
    return gradeMark

# def displayGrades(): # Displays the grading list at the top of console.

def printGrade(grade, mark): # Prints the grade in format.
    # if grade.isdigit():
        # grade = "{0:.2f}".format(grade)
    print(
    """
    Input Grade: {0}
    Grade/Mark: {1}
    Description: {2}
    
    The attained grade of {0} is equivalent to {1}: {2}.
    """.format(grade, mark[0], mark[1])
    )

def main(): # main().
    # displayGrades() # For future formatting of the code.
    
    u_grade = inputGrade()
    u_marking = equateGrade(u_grade)
    u_marking = u_marking.split(":")
   
    printGrade(u_grade, u_marking)
    

while True: # My template for usual main().
    main()
    quit = input("Quit (y/n): ")
    if quit is type(str):
        quit = quit.lower()
        print(quit)
    if (quit == 'y' or quit == 0):
        print("Closing...\n")    
        break
