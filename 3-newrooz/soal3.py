
def khosh_tarif (x) :
    x_2 = [i for i in str(x)]
    x_1 = [int(e) for e in x_2]
    for i in range (len(x_1)) :
        if x_1[i] == x_1[i+1] :
            print("khosh tarif nis")
            break
        else :
            if x_1[i+1] == "?" and x_1[i] == 0 :
                x_1.pop(i+1)
                x_1.insert(i+1,"1")
            elif x_1[i+1] == "?" and x_1[i] == 1 :
                x_1.pop(i+1)
                x_1.insert(i+1,"0")
    print(x_1)


khosh_tarif(101)


