numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0]
# 3
# numbers[-1]
# 2
# numbers[3]
# 1
# numbers[:-1]
# 3, 1, 3, 1, 5, 9
# numbers[3:4]
# 1
# 5 in numbers
# True
# 7 in numbers
# False
# "3" in numbers
# False
# numbers + [6, 5, 3]
#
# Question 1
numbers[0] = "ten"
# Question 2
numbers[-1] = 1
# Question 3
print(numbers[2:])
# Question 4, 1st method
if 9 in numbers:
    print(True)
# Question 4, 2nd method
print(["9 is an element of numbers." for number in numbers if number == 9])
