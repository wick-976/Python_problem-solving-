students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket",
    "Deepak": "Boxing"
}

# Write your code here
update_name=input().split()
students_dict[update_name[0]]=update_name[1]
print(students_dict)