# Initial list
colors = ["Red", "Blue"]

# Using append() to add an item at the end
colors.append("Green")
print("After append():", colors)

# Using insert() to add an item at a specific index
colors.insert(1, "Yellow")  # Insert 'Yellow' at index 1
print("After insert():", colors)


# Initial list
fruits = ["Apple", "Banana", "Cherry", "Banana", "Date"]

# Using pop() to remove by index
fruits.pop()  # Removes last element
print("After pop():", fruits)

# Using pop() with a specific index
fruits.pop(1)  # Removes element at index 1
print("After pop(1):", fruits)

# Using remove() to delete first occurrence of a value
fruits.remove("Banana")
print("After remove('Banana'):", fruits)
