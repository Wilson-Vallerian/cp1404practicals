def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    many_month = int(input("How many months? "))

    for month in range(1, many_month + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    print_report(incomes)


def print_report(incomes):
    """Display Reports of income for each month."""
    total = 0

    for month in range(1, len(incomes) + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:>10.2f}         Total: ${total:10.2f}")


main()
