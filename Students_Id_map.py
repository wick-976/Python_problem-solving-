no_of_students=input().split(",")
no_of_id=input().split(",")


pairs=list(zip(no_of_students,no_of_id))

pairs.sort(key=lambda x: x[0])

for name, sid in pairs:
    print(name, sid)