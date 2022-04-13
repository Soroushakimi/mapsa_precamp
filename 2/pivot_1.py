
from cgitb import reset
from operator import le


my_list = [1,3,4,5,7,3,12,15,19]
my_list_1 = [4,7,12,10,15,20,22]
result = [1]

for i in my_list :
    if i < i+1 :
        result.append(i+1)
    elif i > i+1 :
        break









