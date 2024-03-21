from guitar import Guitar


def main():
    """Sort the displayed guitar based on year of production."""
    FILENAME = "guitars.csv"
    guitars = []

    # from operator import attrgetter
    # in_file = open(FILENAME, "r")
    # for line in in_file:
    #     parts = line.strip().split(",")
    #     guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
    #     guitars.append(guitar)
    # guitars.sort(key=attrgetter("year"))
    # for guitar in guitars:
    #     print(guitar)
    # in_file.close()

    print("Add new guitar")
    name = input("Name: ")
    year = int(input("Year: "))
    price = float(input("Price: "))
    print()
    guitars.append(Guitar(name, year, price))

    in_file = open(FILENAME, "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    in_file.close()

    out_file = open(FILENAME, "w")
    for guitar in guitars:
        print(guitar, file=out_file)
    out_file.close()


main()
