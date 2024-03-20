from prac_06.guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar = Guitar(name, year, cost)
other_guitar = Guitar("Another Guitar", 2015, 1000)
print(guitar)
print()
print(f"{guitar.name} get(age) - Expected 102, got {guitar.get_age()}")
print(f"{other_guitar.name} get_age() - Expected 9, got {other_guitar.get_age()}")
print(f"{guitar.name} is_vintage - Expected True, got {guitar.is_vintage()}")
print(f"{other_guitar.name} is_vintage - Expected False, got {other_guitar.is_vintage()}")
