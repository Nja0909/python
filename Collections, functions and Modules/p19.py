# Function to print a string
def print_string():
    print("Welcome to Python Programming!")

# Calling the function
print_string()

# Lambda function to square a number
square = lambda x: x * x

# Using the lambda function
print("Square of 5:", square(5))

# Lambda function to return sum and product of two numbers
calc = lambda a, b: (a + b, a * b)

# Calling the lambda function
result = calc(4, 5)

print("Sum:", result[0])
print("Product:", result[1])
