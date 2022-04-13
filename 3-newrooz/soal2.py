
my_list = []


def koutah_shavandegi(x) :
    num = 0
    x_1 = [int(i) for i in str(x) ]
    for i in range( len(x_1)-1 ) :
        num1 = x_1[i] + x_1[i+1]
        if num1 > num :
            num = num1
            if i == len(x_1)-2 :
                x_1.remove(x_1[i])
                x_1.remove(x_1[i+1])
                x_1.insert(i,num1)
    print(x_1)

koutah_shavandegi(10038)



