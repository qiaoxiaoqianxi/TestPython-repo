import math
import os
import sys
from os import rename

import requests

#print(sys.version)
#print(sys.executable)

def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting


#print(greet('World'))
#print(greet('Corey'))

r = requests.get("https://www.google.com")
print(r.status_code)'''

#name = input("YOur name? ")
#print("hello,", name)

