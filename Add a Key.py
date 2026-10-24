students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

ans=input().split(" ")
students_dict[ans[0]]=ans[1]

print(students_dict)