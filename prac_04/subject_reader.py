FILENAME = "subject_data.txt"
details = []


def main():
    """Read data from FILENAME and print it out in good-looking way."""
    get_data()
    print()
    display_subject_details()


def display_subject_details():
    """Print subjects details."""
    for i in range(0, len(details)):
        print(f"{details[i][0]} is taught by {details[i][1]:12} and has {details[i][2]:3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        details.append(list(parts))
        print("----------")
    input_file.close()


main()
