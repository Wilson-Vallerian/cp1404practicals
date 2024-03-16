MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50
MENU = "(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Determine star and grade based on valid input."""
    score = get_valid_score()
    grade = determine_grade(score)
    get_valid_choice(score, grade)
    print("Farewell")


def get_valid_choice(score, grade):
    """Get and determine valid choice."""
    print(MENU)
    choice = input(">> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            grade = determine_grade(score)
        elif choice == "P":
            print(f"Grade = {grade}")
        elif choice == "S":
            print("Stars =", "*" * score)
        else:
            print("Invalid Choice")
        print(MENU)
        choice = input(">> ").upper()


def get_valid_score():
    """Get and determine valid score."""
    score = int(input("Enter Score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid Score")
        score = int(input("Enter Score: "))
    return score


def determine_grade(score):
    """Determine grade based on score."""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid Score"
    elif score >= EXCELLENT_SCORE:
        return "Excellent"
    elif score >= PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"


main()
