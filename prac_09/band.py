class Band:
    def __init__(self, band_name):
        """Initialize Band instance"""
        self.band_name = band_name
        self.members = []

    def __str__(self):
        """Return a string representation of Band object."""
        members_str = ", ".join(str(member) for member in self.members)
        return f"{self.band_name} ({members_str})"

    def add(self, musician):
        """Add musician to band."""
        self.members.append(musician)

    def play(self):
        """Display musician details"""
        for member in self.members:
            print(member.play())
