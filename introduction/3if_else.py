a,b,c=input().split()

if int(a)==int(b) and int(a)==int(c):
    print("all of are equal number")

elif int(a)==int(b) and int(a)!=int(c):
    print("1st and 2nd equal")

elif int(a)!=int(b) and int(a)==int(c):
    print("1st and 3rd equal")

elif int(a)!=int(b) and int(b)==int(c):
    print("2nd and 3rd equal")
    
else:
    print("no equal")



