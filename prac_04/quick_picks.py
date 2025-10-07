"""
CP1404/CP5632 Practical
Quick pick program
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("That is an invalid number of picks! please try again")
        number_of_quick_picks = int(input("How many qick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_LINE:
        number = random.randint(MINIMUM, MAXIMUM)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick


main()
