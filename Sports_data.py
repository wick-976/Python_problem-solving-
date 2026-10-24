students_dict = {
    "Ram": "Cricket",
    "Naresh": "Football",
    "Vani": "Tennis",
    "Rahim": "Cricket"
}

# Write your code here
n=int(input())
for i in range(n):
    add=input().split()
    students_dict[add[0]]=add[1]
print(students_dict)