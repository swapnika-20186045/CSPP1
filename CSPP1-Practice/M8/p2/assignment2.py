'''
Author:Swapnika
Created on 06-08-2018
'''
# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number
#and returns the sum of digits of given number.
# This function takes in one number and returns one number.

def sum_digits(nu_m):
    '''
    n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    if nu_m == 0:
        return 0
    return nu_m%10 + sum_digits(nu_m//10)

def main():
    '''main function'''
    a_a = input()
    print(sum_digits(int(a_a)))

if __name__ == "__main__":
    main()
