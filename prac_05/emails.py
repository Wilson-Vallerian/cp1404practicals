def main():
    """Get and store name and email."""
    name_to_email = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        first_name, full_name, last_name = determine_name_part(name)

        validate_name = input(f"Is your name {full_name}? (Y/n) ").lower()

        if validate_name == "y":
            name_to_email[full_name] = email
        else:
            name = input("Name: ")
            first_name, full_name, last_name = determine_name_part(name)
            name_to_email[full_name] = email
        email = input("Email: ")

    print()
    for name, email in name_to_email.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from email."""
    domain = email.find("@")
    name = email[:domain]
    return name


def determine_name_part(name):
    """Determine first name, last name, and full name."""
    try:
        name_parts = name.split(".")
        first_name = name_parts[0].title()
        last_name = name_parts[1].title()
        full_name = f"{first_name} {last_name}"
    except IndexError:
        first_name = name.title()
        last_name = ""
        full_name = first_name
    return first_name, full_name, last_name


main()
