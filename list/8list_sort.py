List=[4,3,8,2,7,4]

#list will sort & print with decending order
List.sort(reverse=True)
print(List)


my_list=['e','w','e','f','s','a']
my_list.sort()
print(my_list)

s_List=[[1,2],[5,9],[3,0],[7,3],[2,3]]

def function(s_List):
    return s_List[1]

s_List.sort(key=function)
print(s_List)


