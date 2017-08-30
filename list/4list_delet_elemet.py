List=[11,22,33,44,55,66,77,88]

#remove  by element
List.remove(11)
print(List)

#delete element by index
del List[3]
print(List)

#delete last element
List.pop()
print(List)

#we can use for delete at index
List.pop(2)
print(List)

#list will be empty
List.clear()
print(List)

#del List
del List
#if we print it will shown error because List has been deleted
#print(List)
