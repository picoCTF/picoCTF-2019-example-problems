#!/usr/bin/python

import string, random

#flag = open("flag", "r").read()
#index = int(open("index", "r").read().strip())

flag = "{{flag}}"
index = {{index}}


for i in range(10000):
    message = random.randint(0,3)
    if (message == 0):
        print "This is not a flag"
    elif(message == 1):
        print "Unfortunately this is also not a flag"
    else:
        print "I'm sorry you're going to have to look at another line"
    if (i == index):
        print flag
