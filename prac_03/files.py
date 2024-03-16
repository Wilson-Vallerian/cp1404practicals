USERNAME_FILE = "name.txt"
NUMBER_FILE = "numbers.txt"


def write_username():
    """Write username to USERNAME_FILE"""
    out_file = open(USERNAME_FILE, "w")
    username = input("Enter Your Name: ")
    print(username, file=out_file)
    out_file.close()


write_username()


def read_username():
    """Read username from USERNAME_FILE"""
    in_file = open(USERNAME_FILE, "r")
    print(f"Your name is {in_file.readline().strip()}")
    in_file.close()


read_username()


def calculate_numbers():
    """Calculate total for 2 Lines in NUMBER_FILE"""
    total_number = 0
    in_file = open(NUMBER_FILE, "r")
    for line in range(0, 2):
        number = int(in_file.readline().strip())
        total_number += number
    print(f"Total numbers = {total_number}")
    in_file.close()


calculate_numbers()


def calculate_all_number():
    """Calculate the total for all lines in NUMBER_FILE"""
    total_number = 0
    in_file = open(NUMBER_FILE, "r")
    for line in in_file:
        total_number += int(line.strip())
    print(f"Total numbers = {total_number}")
    in_file.close()


calculate_all_number()
