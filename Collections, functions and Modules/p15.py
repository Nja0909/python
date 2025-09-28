# Original dictionary
student = {
    "name": "Anjali",
    "age": 20,
    "course": "BCA"
}

# Display original dictionary
print("Before update:", student)

# Updating the value of 'age'
student["age"] = 21

# Display updated dictionary
print("After update:", student)

# Two lists
keys = ["id", "name", "subject"]
values = [101, "Ravi", "Python"]

# Merging using a loop
merged_dict = {}

for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

# Display the resulting dictionary
print("Merged Dictionary:", merged_dict)
