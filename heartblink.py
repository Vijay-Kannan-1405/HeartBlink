from termcolor import colored
import time
from os import system
import cursor 

cursor.hide()

a = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
b = ['red', 'green', 'yellow', 'blue']

def one(x):
    # print(x+1)
    color = str(x)
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(" "*5, colored("*"*4, color), " "*3, colored("*"*4, color))

def two(y):
    color = str(y)
    print(" "*4, colored("*"*6, color), " "*1, colored("*"*6, color))

def three(z):
    color = str(z)
    print(" "*5, colored("*"*13, color))

def four(p):
    color = str(p)
    print(" "*6, colored("*"*11, color))

def five(q):
    color = str(q)
    print(" "*7, colored("*"*9, color))

def six(r):
    color = str(r)
    print(" "*8,colored( "*"*7, color))

def seven(s):
    color = str(s)
    print(" "*9, colored("*"*5, color))

def eight(w):
    color = str(w)
    print(" "*10, colored("*"*3, color))
def nine(n):
    color = str(n)
    print(" "*11, colored("*"*1, color))

# this is main method

def repeat():
    for j in b:

        for i in a:
            l = i + "('" + str(j) + "')"
            exec(l)
        time.sleep(0.8)
        system('cls')
    repeat()
system('cls')
repeat()

# one('red')
