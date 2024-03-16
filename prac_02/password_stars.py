MINIMUM_CHARACTER = 8


def main():
    """Print asterisks based on length of password"""
    password = get_valid_password()
    print_asterisks(password)


def print_asterisks(password):
    """Print asterisks."""
    print("*" * len(password))


def get_valid_password():
    """Get valid password from user."""
    password = input("Enter a password: ")
    while len(password) < MINIMUM_CHARACTER:
        print(f"Password need to be at least {MINIMUM_CHARACTER} characters")
        password = input("Enter a password: ")
    return password


main()
