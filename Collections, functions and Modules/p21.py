# Importing the math module
import math

# Number to demonstrate math functions
num = 9.7

# Using math functions
print("Original number:", num)
print("Square root:", math.sqrt(num))
print("Ceiling value:", math.ceil(num))
print("Floor value:", math.floor(num))
print("Power (2^3):", math.pow(2, 3))
print("Value of pi:", math.pi)

# Importing the random module
import random

# Generating and displaying 5 random numbers between 1 and 100
print("Random numbers between 1 and 100:")
for i in range(5):
    print(random.randint(1, 100))
