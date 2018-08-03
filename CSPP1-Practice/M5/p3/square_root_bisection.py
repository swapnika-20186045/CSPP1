'''
Author:Swapnika
Created on 3-08-2018
'''

def main():
    '''# Write a python program to find the square root of the given number
    using approximation method'''
    sq_r = input()
    epsil_on = 0.01
    #s_p = 0.1
    num_guesses = 0
    lo_w = 0
    hig_h = int(sq_r)
    gu_ess = (hig_h + lo_w)/2.0
    while abs(gu_ess**2 - int(sq_r)) >= epsil_on:
        num_guesses += 1
        if gu_ess**2 < int(sq_r):
            lo_w = gu_ess
        else:
            hig_h = gu_ess
        gu_ess = (hig_h + lo_w)/2.0
    # print('num_guesses=', num_guesses)
    print(num_guesses)
    # print(gu_ess, 'is close to the square root of', sq_r)

if __name__ == "__main__":
    main()
