from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    """Run a taxi simulator program which uses Taxi and SilverServiceTaxi classes."""
    current_taxi = None
    total_bill = 0
    print("Let's drive")
    choice = get_choice()
    while choice != "Q":
        if choice == "C":
            current_taxi = choose_taxi(current_taxi)
        elif choice == "D":
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        choice = get_choice()

    print(f"Total trip cost: ${total_bill}")
    print("Taxis are now: ")
    for i in range(len(taxis)):
        print(f"{i} - {taxis[i]}")


def get_choice():
    """Get user choice."""
    print(MENU)
    choice = input(">>> ").upper()
    return choice


def drive_taxi(current_taxi, total_bill):
    """Drive chosen taxi."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
    else:
        current_taxi.start_fare()
        drive_distance = float(input("Drive how far? "))
        current_taxi.drive(drive_distance)
        taxi_fare = current_taxi.get_fare()
        total_bill += taxi_fare
        print(f"Your Prius trip cost you ${taxi_fare:.2f}")
    return total_bill


def choose_taxi(current_taxi):
    """Determine which taxi to choose."""
    print("Taxis available: ")
    for i in range(len(taxis)):
        print(f"{i} - {taxis[i]}")
    try:
        taxi_choice = int(input("Choose Taxi: "))
        current_taxi = taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")
    except ValueError:
        print("Invalid taxi choice")
    return current_taxi


main()

