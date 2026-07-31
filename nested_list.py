n=int(input())
list1=[]

for _ in range(n):
    row=list(map(int, input().split()))
    list1.append(row)
print(list1)