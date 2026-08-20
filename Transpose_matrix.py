def get_transpose_of_matrix(matrix, m, n):
    transpose=[]
    
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(0)
        transpose.append(row)
        
    for i in range(m):
        for j in range(n):
            transpose[j][i]=matrix[i][j]
    for row in transpose:
        print(row)

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

get_transpose_of_matrix(num_list,m,n)