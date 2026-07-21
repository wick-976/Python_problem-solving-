n=list(map(int,input().split()))

odd_index=[]
occurance=0;
for num in n:
    if n.count(num) %2!=0:
        odd_index.append(num)
odd_index=sorted(set(odd_index))
print(odd_index)
        

    