"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)


def load_subjects(filename=FILENAME):
    """Load subject data from file into a list of: code, lecturer, students."""
    subjects = []
    input_file = open(FILENAME)
    for line in input_file:
        parts = line.strip().split(',')
        parts[2] = int(parts[2])  # convert student number from str to int
        subjects.append(parts)
    input_file.close()
    return subjects


def display_subjects(subjects):
    """Display subject details in a readable format."""
    for subject in subjects:
        print("{} is taught by {:12} and has {:3} students".format(*subject))


main()
