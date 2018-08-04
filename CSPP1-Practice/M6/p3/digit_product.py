'''
Author : Swapnika
Created on 4-08-2018
'''

def main():
    '''Given a number int_input, find the product of all the digits example:
    input: 123
    output: 6
    '''
    nu_m = int(input())
    pr_o = 1
    while nu_m > 0:
        re_s = nu_m%10
        pr_o = pr_o * re_s
        nu_m = nu_m // 10
    print(pr_o)
if __name__ == "__main__":
    main()
