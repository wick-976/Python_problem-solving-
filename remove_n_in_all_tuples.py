num_list = [(1, 2, 3, 4, 5, 6), (2, 4, 6, 8), (1, 3, 5, 7)]
# Write your code here
n=int(input())
for i in range(len(num_list)):
    s=set(num_list[i])
    if n in s:
        s.remove(n)
    num_list[i]=tuple(s)
print(num_list)