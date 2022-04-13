
my_list = [1,2,5,4,6,8,9,4,12,34,56,10]
result = []

for i in range(len(my_list)-2) :
    if my_list[i] < my_list [i+1] and my_list [i+1] > my_list [i+2] :
        result.append(i)
    elif my_list [i] > my_list [i+1] and my_list [i+1] < my_list [i+2] :
        result.append(i)


print(len(result))




