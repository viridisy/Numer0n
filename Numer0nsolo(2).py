from __future__ import print_function, unicode_literals
from PyInquirer import prompt, Separator
import random
import math


def int_input():
    print()
    while True:
        i=input() 
        if i.isdecimal():
            i = int(i)
            break
    return i

def ndigint_input(n):
    while True:
        i=int_input()
        if 10**(n-1)<=i and i<10**n:
            break
        print("Input "+str(n)+" digit number!")
    return i    

def rannum():
    return math.floor(10*random.random())

def printm(i):
    print("")
    for n in range(len(i)+4):
        print("-", end="")
    print("")
    print("  "+i+"  ")
    
    for n in range(len(i)+4):
        print("-", end="")
    print("")

print("Numer0n\n")
while True:
    commands = [
        {
            "type": "list",
            "message": "Input next command",
            "choices": [
                "New game", 
                "Quit"
            ]
        }
    ]
    com = prompt.prompt(commands)
    if(com=="New game"):
        key = []
        for i in range(3):
            while True:
                k = rannum()
                if (not k in key):
                    key.append(k)
                    break

        ans = []
        while (not ans==key):
            
            eat = 0
            bite = 0
            while True:
                print()
                printm("Input your answer in three digits!")
                ansnum=ndigint_input(3)
                ans=[ansnum%(10**(i+1))//(10**i) for i in reversed(range(3))]
                if(ans[0]!=ans[1] and ans[1]!=ans[2] and ans[2]!=ans[0]):
                    break
                else:
                    printm("Each digit must be distinct!")
            for i in range(3):
                if ans[i]==key[i]:
                    eat=eat+1
                elif ans[i] in key:
                    bite=bite+1
            printm("Your answer : "+str(ans)+", "+str(eat)+" eat, "+str(bite)+" bite")


        printm("you win")
    elif(com=="Quit"):
        printm("You quit")
        exit()
