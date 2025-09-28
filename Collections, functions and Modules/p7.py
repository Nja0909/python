# Define a list of fruits
fruits = ["Apple", "Banana", "Cherry", "Date", "Fig"]

# Iterate using a for loop
print("List of fruits:")
for fruit in fruits:
    print(fruit)

# Original list of numbers
numbers = [45, 12, 89, 33, 7]

# Using sort() method (modifies the original list)
numbers.sort()
print("List after sort():", numbers)

# Reset the list
numbers = [45, 12, 89, 33, 7]

# Using sorted() function (returns a new sorted list)
sorted_list = sorted(numbers)
print("Original list after using sorted():", numbers)
print("New sorted list:", sorted_list)
