'''
Author:Swapnika
Created on 06-08-2018
'''
# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number
#and returns the factorial of given number.
# This function takes in one number and returns one number.

def fact_orial(nu_m):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if nu_m in (1, 0):
        return 1
    return nu_m*fact_orial(nu_m-1)

def main():
    '''main function'''
    a_val = input()
    print(fact_orial(int(a_val)))

if __name__ == "__main__":
    main()
