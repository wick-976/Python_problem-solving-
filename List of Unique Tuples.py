n=int(input())
set1=[]
for i in range(n):
    list1=list(map(int,input().split()))

    if len(list1) == len(set(list1)):
        set1.append(list1)
print(set1)