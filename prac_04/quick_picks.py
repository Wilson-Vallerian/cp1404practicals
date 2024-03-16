import random
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_LINE = 6
NO_LINE = 0


def main():
    """Print random numbers in sorted form."""
    many_line = determine_valid_line()

    for line in range(many_line):
        numbers = []
        for number in range(NUMBERS_PER_LINE):
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            numbers.append(random_number)
            numbers.sort()
        for number in numbers:
            print(f"{number:2}", end=" ")
        print(end="\n")


def determine_valid_line():
    """Get valid line."""
    many_line = int(input("How many Quick Picks? "))
    while many_line < NO_LINE:
        print("Line must be greater or equals to 0!")
        many_line = int(input("How many Quick Picks? "))
    return many_line


main()
