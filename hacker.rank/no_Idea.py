
#n = int (input())
#m = int (input())


n , m = [ int(x) for x in input().split() ]

x = list (map (int , input () .strip() .split())) [:n]

print(x)

A = list (map (int , input () .strip() .split())) [:m]

#A = set(A)

B = list (map (int , input () .strip() .split())) [:m]

#B = set(B)
total = -1

for i in range(len(A)) :
    if A[i] in x :
        total = total + 1
    elif B[i] in x :
        total = total -1
 
print(total)



