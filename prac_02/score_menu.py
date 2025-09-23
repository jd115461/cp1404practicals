MENU = """G - Get a valid score
P - Print result
S - Show stars
Q - Quit"""


def main():
    score = get_valid_score()
    print("MENU: ")
    choice = input("> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_result_status(score))
        elif choice == "S":
            print(print_stars(score))
        else:
            print("Invalid choice")
        print("Menu: ")
        choice = input("> ").upper()
    print("Goodbye")


def get_valid_score():
    score = int(input("Enter score: "))
    while score > 100 or score < 0:
        print("invalid score")
        score = int(input("Enter score: "))
    return score


def determine_result_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    print("*" * score)


main()
