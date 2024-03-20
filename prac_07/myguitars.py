from guitar import Guitar


def main():
    """Sort the displayed guitar based on year of production."""
    # from operator import attrgetter
    # guitars = []
    # FILENAME = "guitars.csv"
    # in_file = open(FILENAME, "r")
    # for line in in_file:
    #     parts = line.strip().split(",")
    #     guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
    #     guitars.append(guitar)
    # guitars.sort(key=attrgetter("year"))
    # for guitar in guitars:
    #     print(guitar)
    # in_file.close()

    guitars = []
    FILENAME = "guitars.csv"
    in_file = open(FILENAME, "r")
    for line in in_file:
        parts = line.strip().split(",")
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    in_file.close()


main()