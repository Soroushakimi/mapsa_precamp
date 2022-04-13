
my_list = []

def delete_local_maximum (x) :
    changes = 0
    for i in range (len(x)-2) :
        if x[i+1] > x[i] and x[i+1] > x[i+2] :
            x[i+2] = x[i+1]
            changes = changes +1
            x.remove(x[i+2])
            x.insert(i+2,x[i+1])
    print(changes)
    print(x)


delete_local_maximum([2,1,3,1,3,1,3,1,3])



