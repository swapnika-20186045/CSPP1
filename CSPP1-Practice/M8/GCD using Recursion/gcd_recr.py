'''
Author:Swapnika
Created on 06-08-2018
'''
# Exercise: GCDRecr
# Write a Python function, gcdRecur(a, b), that takes in two numbers
#and returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number.

def gcd_recur(a_a, b_b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    min_val = min(a_a, b_b)
    if min_val == a_a:
        a_a, b_b = b_b, a_a
    if a_a%b_b == 0:
        return b_b
    return gcd_recur(b_b, a_a%b_b)

def main():
    '''main funtion'''
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
