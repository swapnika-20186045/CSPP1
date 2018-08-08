'''
Author: Swapnika
Created on 08-08-2018
'''
#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given
#testList = [1, -4, 8, -9] into [1, 16, 64, 81]

def square(x):
    return x**2

def apply_to_each(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L
    
def main():
    '''main function'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    output = apply_to_each(list1, square)
    print (output)

if __name__== "__main__":
    main()