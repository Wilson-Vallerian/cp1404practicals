MINIMUM_SALES = 0
BONUS_THRESHOLD = 1000
LOW_BONUS_PERCENTAGE = 10
HIGH_BONUS_PERCENTAGE = 15
PERCENT = 100

sales = float(input("Enter sales: $"))
while sales >= MINIMUM_SALES:
    if sales < BONUS_THRESHOLD:
        bonus_percentage = LOW_BONUS_PERCENTAGE
    else:
        bonus_percentage = HIGH_BONUS_PERCENTAGE
    bonus = sales * bonus_percentage / PERCENT
    print(f"Bonus = {bonus}")
    sales = float(input("Enter sales: $"))
