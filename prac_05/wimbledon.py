"""
Emails
Estimate: 21 minutes 26 seconds 760 millisecond
Actual:  22 minutes  16 seconds 450 millisecond
"""

FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    """Read the data file and print details about Wimbledon champions and countries"""
    records = load_records(FILENAME)
    champion_to_count, countries = analyse_records(records)
    display_results(champion_to_count, countries)


def analyse_records(records):
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_to_count[record[INDEX_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_CHAMPION]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display record results as champions and countries"""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))


def load_records(filename):
    """Load records from file"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
        return records


main()
