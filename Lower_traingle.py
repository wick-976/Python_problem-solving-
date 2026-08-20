def print_lower_triangle(matrix,m,n):
    result=[]
    for i in range(m):
        row=[]
        for j in range(min(i+1,n)):
           row.append(matrix[i][j])
        result.append(row)
    return result
    

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)

# Call the print_lower_triangle function
lower_traingle=print_lower_triangle(num_list,m,n)

for row in lower_traingle:
    print(row)