import random
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50


def main():
    """Print grade based on valid score and print grade form random score."""
    score = float(input("Enter score: "))
    result = determine_grade(score)
    print(f"Result = {result}")
    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(f"Random Score = {random_score}")
    result = determine_grade(random_score)
    print(f"Result = {result}")


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
