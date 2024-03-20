from prac_06.guitar import Guitar


def main():
    """Print Guitar name, year and cost based on user input"""
    guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]

    print("My guitars!")
    get_valid_information(guitars)

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_word = ""
            if guitar.is_vintage():
                vintage_word = " (vintage)"
            print("Guitar {0}: {1.name:>14} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, vintage_word))


def get_valid_information(guitars):
    """Get a valid guitar name, year, and cost."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")


main()
