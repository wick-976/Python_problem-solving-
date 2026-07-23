num_list = [(10, 20, 30), (1, 2), (5, 10, 15, 45)]
# Write your code here
n=int(input())
for i in range(len(num_list)):
    temp=list(num_list[i])
    temp[-1]=n
    num_list[i]=tuple(temp)
print(num_list)
