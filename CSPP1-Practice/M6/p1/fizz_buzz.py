'''
Author : Swapnika
Created on 4-08-2018
'''

def main():
    '''
    Write a short program that prints each number from 1 to num on a new line.
    For each multiple of 3, print "Fizz" instead of the number.
    For each multiple of 5, print "Buzz" instead of the number.
    For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
    '''
    nu_m = int(input())
    for i in range(1, nu_m + 1):
        if i%3 == 0 and i%5 == 0:
            print("Fizz")
            print("Buzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    main()
