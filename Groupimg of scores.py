one=input()

parts=one.split(",")

s_dict={}

for item in parts:
    key, value=item.split(":")
    value=int(value)
    if key in s_dict:
        s_dict[key]+=value
    else:
        s_dict[key]=value

result=sorted(s_dict.items())
print(result)