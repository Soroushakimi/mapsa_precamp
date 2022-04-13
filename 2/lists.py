
from posixpath import split


def swap_case(s):
    my_list = []
    for i in s :
        if i.islower() :
            my_list.append(i.upper())
        if i.isupper() :
            my_list.append(i.lower())
    print(" ".join(my_list))

swap_case("Soroush Hakimi")
