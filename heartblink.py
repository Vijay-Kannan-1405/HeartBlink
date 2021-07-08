from termcolor import colored
import time
from os import system
import cursor 

cursor.hide()

a = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twele']
b = ['red', 'green', 'yellow', 'blue']

def one(x):
    # print(x+1)
    color = str(x)
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(" "*42, colored("*"*8, color), " "*3, colored("*"*8, color))

def two(y):
    color = str(y)
    print(" "*39, colored("*"*12, color), " "*1, colored("*"*12, color))

def three(z):
    color = str(z)
    print(" "*38, colored("*"*29, color))

def four(p):
    color = str(p)
    print(" "*39, colored("*"*27, color))

def five(q):
    color = str(q)
    print(" "*40, colored("*"*25, color))

def six(r):
    color = str(r)
    print(" "*41,colored( "*"*23, color))

def seven(s):
    color = str(s)
    print(" "*43, colored("*"*19, color))

def eight(w):
    color = str(w)
    print(" "*45, colored("*"*15, color))
def nine(n):
    color = str(n)
    print(" "*47, colored("*"*11, color))
def ten(n):
    color = str(n)
    print(" "*49, colored("*"*7, color))
def eleven(n):
    color = str(n)
    print(" "*51, colored("*"*3, color))
def twele(n):
    color = str(n)
    print(" "*52, colored("*"*1, color))

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
