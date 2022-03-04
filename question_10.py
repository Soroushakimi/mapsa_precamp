
from cgi import print_form
from doctest import master


message = "Babak Khorramdin"

print(message[0]) # الف

print(message[6]) # ب

print(message.split()) # پ

print(message[0:13:2]) # ت

for m in message :
    if m == "m" :
        print(True)
        break


