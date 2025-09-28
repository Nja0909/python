# Creating a tuple with multiple data types
my_tuple = (25, "Hello", 3.14, True, None, [1, 2, 3], ("a", "b"))

# Printing the tuple
print("Tuple with multiple data types:")
print(my_tuple)

# Printing the type of each element in the tuple
print("\nData types of each element:")
for element in my_tuple:
    print(f"{element} --> {type(element)}")



# First tuple
tuple1 = (1, 2, 3)

# Second tuple
tuple2 = ("a", "b", "c")

# Concatenating the two tuples
combined_tuple = tuple1 + tuple2

# Printing the result
print("First Tuple:", tuple1)
print("Second Tuple:", tuple2)
print("Concatenated Tuple:", combined_tuple)
