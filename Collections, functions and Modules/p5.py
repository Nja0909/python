# Creating a list
my_list = ["Apple", "Banana", "Cherry", "Banana", "Date"]

# Removing elements using pop()
last_item = my_list.pop()  # Removes last element
print("List after pop():", my_list)
print("Popped item:", last_item)

# Removing element at index 1
my_list.pop(1)
print("List after pop(1):", my_list)

# Removing elements using remove()
my_list.remove("Banana")  # Removes first occurrence of 'Banana'
print("List after remove('Banana'):", my_list)
