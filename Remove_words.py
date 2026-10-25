word=input().split(" ")
no=int(input())

for item in word:
    if(len(item)!=no):
        print(item,end=" ")