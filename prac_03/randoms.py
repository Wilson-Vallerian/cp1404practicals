import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# The random.randint is to generate a random integer number between 5 and 20 with the increment of 1
# What was the smallest number you could have seen, what was the largest?
# The smallest number is 5 while the largest number is 19.
# What did you see on line 2?
# The random.randrange is to generate a random integer number between 3 and 10 with the increment of 2 that is 3, 5, 7, 9.
# What was the smallest number you could have seen, what was the largest?
# The smallest number is 3 while the largest number is 9.
# Could line 2 have produced a 4?
# No.
# What did you see on line 3?
# The random.uniform is to generate a random float number between 2.5 and 5.5..
# What was the smallest number you could have seen, what was the largest?
# The smallest number is 2.5 while the largest number is 5.49.
#
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(0, 101))
