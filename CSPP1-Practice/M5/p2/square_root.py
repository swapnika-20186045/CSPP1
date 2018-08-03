'''
Author:Swapnika
Created on 3-08-2018
'''

def main():
    '''Write a python program to find the square root of the given number
    using approximation method'''
    sq_r = input()
    epsilon = 0.01
    guess = 0.0
    increment = 0.1
    num_guesses = 0
    while abs(guess**2 - int(sq_r)) >= epsilon:
        guess += increment
        num_guesses += 1
    #print('num_guesses=', num_guesses)
    if abs(guess**2 - int(sq_r)) >= epsilon:
        print('Failed on square root of', sq_r)
    else:
        print(guess)

if __name__ == "__main__":
    main()
