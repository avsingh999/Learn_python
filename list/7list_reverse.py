List=[11,22,33,44,55,66,77,88]

print("1st method")
List.reverse()
print(List)

#*********
my_list=['a','e','i','o','u']

print("2nd method")
revr=my_list[::-1]
print(revr)

print("3rd method")
print(list(reversed(my_list)))

print("4th method")
for i in reversed(my_list):
    print(i)
