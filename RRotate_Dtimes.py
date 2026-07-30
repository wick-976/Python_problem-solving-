arr=list(map(int,input().split(',')))
d=int(input())

n=len(arr)
d=d%n
rotated=arr[d:]+arr[:d]

print(list(rotated))