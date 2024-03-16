FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Read and print details about Wimbledon champions and countries from FILENAME."""
    records = load_records(FILENAME)
    champion_to_count, winner_countries = process_records(records)
    display_results(champion_to_count, winner_countries)


def load_records(filename):
    """Get records from file in list form."""
    records = []
    in_file = open(filename, "r", encoding="utf-8-sig")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(",")
        records.append(parts)
    in_file.close()
    return records


def process_records(records):
    """Create dictionary to count how many times the team have won and set for winner countries."""
    winner_countries = set()
    champion_to_count = {}
    for record in records:
        winner_countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_count[record[CHAMPION_INDEX]] = 1
    return champion_to_count, winner_countries


def display_results(champion_to_count, winner_countries):
    """Print Wimbledon champions, many wins, and sorted winner countries."""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"These {len(winner_countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(winner_countries)))


main()
