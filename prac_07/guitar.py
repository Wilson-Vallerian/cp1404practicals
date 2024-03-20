CURRENT_YEAR = 2024
VINTAGE_YEAR = 50


class Guitar:

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __repr__(self):
        return str(self)

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_YEAR

    def __lt__(self, other):
        return self.year < other.year


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
