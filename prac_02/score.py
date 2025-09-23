"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import randint

def main():
    grade_score = float(input("Enter score: "))
    print(determine_result_status(grade_score))
    random_score = randint(0, 100)
    print(f"Random score is: {random_score} ")


def determine_result_status(grade_score):
    if grade_score < 0 or grade_score > 100:
        return "Invalid score"
    elif grade_score >= 90:
        return "Excellent"
    elif grade_score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
