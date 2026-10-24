new_dict={}

first_name=input().split(" ")
first_value=list(map(int, input().split(" ")))
second_name=input().split(" ")
second_value=list(map(int, input().split(" ")))

dict1=dict(zip(first_name,first_value))
dict2=dict(zip(second_name,second_value))

combined={**dict1, **dict2}
result=list(combined.items())
result.sort(key=lambda x: x[0])

print(result)


    