
from ast import Num


num = int( input() )
asami = {}
for i in range(num) :
    name = input()
    score_1 , score_2 , score_3 = input ().split()
    total = (int (score_1) + int (score_2) + int (score_3 )) / 3
    asami[name] = total

print(asami)



