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

def onedigint_input():
    while True:
        i=int_input()
        if 0<=i<10:
            break
        print("input again!")
    return i    

def rannum():
    return math.floor(10*random.random())


print("Numer0n\n")

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
    print("input your answer")
    ans=[onedigint_input(), onedigint_input(), onedigint_input()]
    for i, num in enumerate(ans):
        if ans[i]==key[i]:
            eat=eat+1
        elif ans[i] in key:
            bite=bite+1
    print("Your answer : "+str(ans)+", "+str(eat)+" eat, "+str(bite)+" bite")


print("you win")