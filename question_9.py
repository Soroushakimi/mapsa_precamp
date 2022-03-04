
length = int (input("length : "))
height = int (input("height : "))
n = 1

for i in range(height) :
    if i == 0  :
        print(" " * length + "* " * length)
    elif i == height - 1 :
        print(" " + " *" * length)
    else :
        space = " " * (length - n)
        print(space + "* " + (" " * (length -2)) + "   *")
        n += 1


