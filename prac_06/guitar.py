CURRENT_YEAR = 2024
VINTAGE_YEAR = 50


class Guitar:
    """Represent a guitar object."""
    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Defines the string representation."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Determine guitar age."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage."""
        return self.get_age() >= VINTAGE_YEAR

