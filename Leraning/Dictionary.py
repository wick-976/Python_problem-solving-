#this for creating Dictionary


dict_a={
    "Name":"Tharan",
    "age":20,
    "town":"Pollachi"
}

print(dict_a)
print(dict_a['Name'])
print(dict_a['age'])


print(dict_a.get('Name'))

message='Name' in dict_a
print(message)

dict_a['city']='Coimbatore'
print(dict_a)

del dict_a['age']
print(dict_a)

print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())


for keys in dict_a.keys():
  print(keys)

print(list(dict_a.keys())) 