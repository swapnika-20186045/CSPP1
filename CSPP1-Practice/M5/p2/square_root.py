'''
Author:Swapnika
Created on 3-08-2018
'''

def main():
    '''Write a python program to find the square root of the given number
    using approximation method'''
    sq_r = input()
    epsil_on = 0.01
    gu_ess = 0.0
    st_ep = 0.1
    num_guesses = 0
    while abs(gu_ess**2 - int(sq_r)) >= epsil_on:
        gu_ess += st_ep
        num_guesses += 1
    #print('num_guesses=', num_guesses)
    if abs(gu_ess**2 - int(sq_r)) >= epsil_on:
        print('Failed on square root of', sq_r)
    else:
        print(gu_ess)

if __name__ == "__main__":
    main()
