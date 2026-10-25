a=input()
words=""
number=""
for i in range(len(a)):
    if a[i]>='a' and a[i] <='z':
        words+=a[i]
    else:
        number+=a[i]
print(words+number)