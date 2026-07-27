num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Write your code here
list3=set(map(int,input().split()))
if num_set.issuperset(list3):
    print("Superset")
elif num_set.issubset(list3):
    print("Subset")
elif num_set.isdisjoint(list3):
    print("Disjoint Set")
