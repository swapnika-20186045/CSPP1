'''
Author: Swapnika
Created on 1-8-2018
'''

VARA = input("enter something")
VARB = input("enter something")
if isinstance(VARA) == str or isinstance(VARB) == str:
    print("strings involved")
if VARA > VARB:
    print("bigger")
elif VARA == VARB:
    print("equal")
else:
    print("smaller")
