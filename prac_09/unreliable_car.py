from prac_09.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability: float):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive car based on their reliability."""
        random_number = random.randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        drive_distance = super().drive(distance)
        return drive_distance
