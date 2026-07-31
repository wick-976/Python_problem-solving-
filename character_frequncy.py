string=input().replace(" ","")
string=sorted(string)


arr=[0]*27

for ch in string:
    idx=ord(ch.lower())-ord('a')
    if 0<=idx<26:
        arr[idx] +=1
        
for i in range(26):
    if arr[i] > 0:
        print(f"{chr(i + ord('a'))}: {arr[i]}")
