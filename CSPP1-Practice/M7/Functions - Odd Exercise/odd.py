'''
Author:Swapnika
Created on 06-08-2018
'''

def odd(x):
    '''
    x: int or float.
    Write a Python function, odd, that takes in one number and returns True when the number is odd and False otherwise.
    returns: True if x is odd, False otherwise
    '''
    return x%2 != 0
    

def main():
    data = input()
    print(odd(int(data)))

if __name__ == "__main__":
    main()
