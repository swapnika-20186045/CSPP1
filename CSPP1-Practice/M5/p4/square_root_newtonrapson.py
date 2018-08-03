'''
Author: Swapnika
Created on 3-08-2018
'''

def main():
    '''Write a python program to find the square root of the number
    using Newton-Rapson method'''
    epsilon = 0.01
    sq_r = input()
    guess = int(sq_r)/2.0
    num_guesses = 0
    while abs(guess*guess - int(sq_r)) >= epsilon:
        num_guesses += 1
        guess = guess -(((guess**2) - int(sq_r))/(2*guess))
    print('num_guesses = '+" "  +str(num_guesses))
    print('Square root of' + str(sq_r) + ' is about ' + str(guess))

if __name__ == "__main__":
    main()
