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
for i in range(len(num_list)):
    maxi=max(max(x[i]) for x in num_list)
    mini=min(min(x[i]) for x in num_list)
    summation=sum(sum(x[i]) for x in num_list)
print(maxi)
print(mini)
print(summation)
