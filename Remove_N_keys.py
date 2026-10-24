alphabets = {
    'a': 97,
    'b': 98,
    'c': 99,
    'd': 100,
    'e': 101,
    'f': 102,
    'g': 103,
    'h': 104,
}

# Write your code here
n=input().split(" ")
length=len(n)
for item in n:
    if item in alphabets:
        del alphabets[item]
print(alphabets)