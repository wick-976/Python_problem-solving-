num1=input().split(",")
num2=input().split(",")

tem1=set(map(int,num1))
tem2=set(map(int,num2))
ans=tem1 & tem2
answer=sorted(list(ans))
print(answer)




