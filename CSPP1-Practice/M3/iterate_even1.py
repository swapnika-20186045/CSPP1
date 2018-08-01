'''
Author: Swapnika
Created on 1-8-2018
'''

N = int(input("enter the number"))
for I in range(0, 12, 2):
    if I%2 == 0:
        print(I)
    I = I+2
print("Goodbye")
