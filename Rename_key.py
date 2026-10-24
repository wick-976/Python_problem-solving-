fruits = {
    "apples": 10,
    "bananas": 20,
    "mangoes": 15,
    "oranges": 200,
    "watermelons": 50
}

# Write your code here
old=input()
new=input()

result=[]

for k,v in fruits.items():
    if k==old:
        result.append((new, v))
    else:
        result.append((k, v))
        
print(result)