"""
CP1404/CP5632 Practical

"""

from guitar import Guitar
FILENAME = "guitars.csv"

def main():
    """Load guitars from CSV file, display them, sort them by year and then display again."""
    guitars = load_guitars(FILENAME)
    print("These are my guitars:")
    display_guitars(guitars)
    guitars.sort()
    print("\nHere are my guitars sorted from oldest to newest:")
    display_guitars(guitars)


def load_guitars(filename):
    """Load guitars from the CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            name, year, cost = line.strip().split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars

def display_guitars(guitars):
    """Display all guitars in a formatted list."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


if __name__ == "__main__":
    main()