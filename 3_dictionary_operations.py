student = {"Name": "Insha", "Roll_no": 55, "Marks": 85}

print("Dictionary:", student)
print("Name:", student["Name"])
print("Roll_no:", student["Roll_no"])
print()

print("2. Update Elements")
student["Marks"] = 90
student["Grade"] = "A"
print("Updated Dictionary:", student)
print()

print("3. Removing Elements")
removed_value = student.pop("Grade")
print("Removed Value:", removed_value)
print("After Removing 'Grade':", student)

student.popitem()
print("After popitem():", student)
print()

print("4. Merging Dictionaries")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2
print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Merged Dictionary:", merged_dict)
