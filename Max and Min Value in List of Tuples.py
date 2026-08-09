n=int(input())
anser=[]
for i in range(n):
    s=tuple(map(int,input().split()))
    anser.append(s)

max_0=max(x[0] for x in anser)
max_3=min(x[0] for x in anser)

max_4=max(x[1] for x in anser)
max_5=min(x[1] for x in anser)

print((max_0,max_3))
print((max_4,max_5))

