
a,b,c = [int(a) for a in input("enter 3 numbers : ").split()]

if a > b and a > c :
    print("max is : " , a)
elif b > a and b > c :
    print("max is : " , b)
else :
    print("max is : " , c)
if a < b and a < c :
    print("min is : " , a)
elif b < a and b < c :
    print("min is : " , b)
else :
    print("min is : " , c)




