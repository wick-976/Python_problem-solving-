string=input().split()
temp=True
set1=set(string)
for i in range(1,len(string)):
    if(string[0]!=string[i]):
        temp=False
        
if(temp):
    print(temp)
else:
    print(sorted(list(map(int,set1))))
        
          