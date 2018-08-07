'''
Author:Swapnika
Created on 06-08-2018
'''
# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers
#and returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number.

def gcd_iter(a_a, b_b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a_a > b_b:
        min_val = b_b
    else:
        min_val = a_a
    for i in range(1, min_val+1):
        if (a_a%i == 0 and b_b%i == 0):
            gcd = i
    return gcd

def main():
    '''main function'''
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
