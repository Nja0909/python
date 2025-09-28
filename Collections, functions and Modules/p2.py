# Creating a list
my_list = ["apple", "banana", "cherry", "banana", "date"]

# Using pop() to remove by index
removed_item = my_list.pop()   # Removes last item
print("After pop():", my_list)
print("Popped item:", removed_item)

# Using pop() with specific index
my_list.pop(1)  # Removes element at index 1 (banana)
print("After pop(1):", my_list)

# Using remove() to remove by value
my_list.remove("banana")  # Removes first occurrence of "banana"
print("After remove('banana'):", my_list)
