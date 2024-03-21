class ProgrammingLanguage:
    """Represent a programming language."""
    def __init__(self, field="", typing="", reflection="", year=""):
        """Initialise a programming language instance."""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Defines the string representation."""
        return f"{self.field}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}"

    def __repr__(self):
        """Return string for list."""
        return str(self)

    def is_dynamic(self):
        """Determine if a programming language is dynamic."""
        return self.typing == "Dynamic"
