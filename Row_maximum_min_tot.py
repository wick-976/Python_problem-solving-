def print_max_min_sum_for_row_wise(num_list):
    maximum=[]
    minimum=[]
    tot=[]
    for row in num_list:
        maximum.append(max(row))
        minimum.append(min(row))
        tot.append(sum(row))
    print(maximum)
    print(minimum)
    print(tot)
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

print_max_min_sum_for_row_wise(num_list)
