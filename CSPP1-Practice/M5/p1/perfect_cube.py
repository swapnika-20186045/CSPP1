'''
Author:Swapnika
Created on 3-08-2018
'''

def main():
    '''Write a python program to find if the given number is a perfect cube or not
    using guess and check algorithm'''
    print("enter an integer: ")
    nu_m = input()
    ans = 0
    while ans ** 3 < int(nu_m):
        ans = ans + 1
    if ans ** 3 == int(nu_m):
        print(str(nu_m) + ' is a perfect cube')
    else:
        print(str(nu_m) + ' is not a perfect cube')

if __name__ == "__main__":
    main()
