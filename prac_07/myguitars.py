"""
CP1404/CP5632 Practical
My guitars - Read CSV, display results, sort in old to new and save back to the CSV file.
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
    add_guitars(guitars)
    save_guitars(FILENAME, guitars)
    print(f"\nGuitars saved to {FILENAME}.")


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


def add_guitars(guitars):
    """Prompt user to add new guitars and append them to the list."""
    print("\nAdd new guitars: ")
    name = input("Name: ").strip()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ").strip()


def save_guitars(filename, guitars):
    """Save added guitars to the CSV file."""
    with open(filename, "w", encoding="utf-8-sig") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


if __name__ == "__main__":
    main()
