# Dictionary before update
employee = {
    "name": "Rahul",
    "age": 28,
    "department": "Sales"
}

# Display original dictionary
print("Before update:", employee)

# Updating the value of 'department'
employee["department"] = "Marketing"

# Display updated dictionary
print("After update:", employee)

# Sample dictionary
student = {
    "name": "Meera",
    "age": 19,
    "course": "BCA"
}

# Separating keys and values
keys = list(student.keys())
values = list(student.values())

# Display results
print("Keys:", keys)
print("Values:", values)

# Lists
keys = ["id", "name", "subject"]
values = [102, "Ankita", "Computer Networks"]

# Convert lists to dictionary using loop
result = {}
for i in range(len(keys)):
    result[keys[i]] = values[i]

# Display the dictionary
print("Resulting Dictionary:", result)

# Input string
text = "dictionary"

# Initialize empty dictionary
char_count = {}

# Count character occurrences
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

# Display result
print("Character Count:")
for char, count in char_count.items():
    print(f"{char}: {count}")
