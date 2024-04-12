from prac_09.taxi import Taxi


def main():
    """Simulates a test scenario for the Taxi class."""
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    taxi.get_fare()
    print(f"{taxi}, fare = {taxi.get_fare()}")
    taxi.start_fare()
    taxi.drive(100)
    taxi.get_fare()
    print(f"{taxi}, fare = {taxi.get_fare()}")


main()
