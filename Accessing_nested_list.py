list_a = [('apple', 'banana', 'orange', 'grapes'), ('cricket', 'football', 'hockey'), ('car', 'bicycle', 'bus')]
# Write your code here
n=int(input())
result=[]
for i in range(n):
    
    s=list(map(int,input().split()))
    result.append(list_a[s[0]][s[1]])
print(result)