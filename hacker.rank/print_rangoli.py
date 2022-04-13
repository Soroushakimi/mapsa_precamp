import string
from typing import Sized
from xmlrpc.server import SimpleXMLRPCDispatcher


def print_rangoli (size) :
    for i in range(size*2-1) :
        letters = list(string.ascii_lowercase)
        print("-" * (size*2-2) + letters[size-1] + "-" * (size*2-2) )
        size = size - 1


print_rangoli(5)



