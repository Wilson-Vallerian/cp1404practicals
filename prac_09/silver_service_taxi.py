from prac_09.taxi import Taxi
FLAGFALL = 4.50


class SilverServiceTaxi(Taxi):
    """Run SilverServiceTaxi service."""
    def __init__(self, name, fuel, fanciness: float):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${FLAGFALL}"

    def get_fare(self):
        """Get current fare."""
        return super().get_fare() + FLAGFALL
