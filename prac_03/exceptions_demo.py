"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When either the numerator or denominator is not integer.
2. When will a ZeroDivisionError occur?
When the denominator is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
The other option we could use is the if else function to check if the denominator is not 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Denominator couldn't be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
