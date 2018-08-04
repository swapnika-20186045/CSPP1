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
    c_nt = 0
    k = nu_m
    while nu_m != 0:
        c_nt += 1
        nu_m = nu_m // 10
    tem_p = k
    while tem_p > 0:
        re_s = tem_p % 10
        pr_o = pr_o * (re_s)
        tem_p = tem_p // 10
    print(pr_o)
if __name__ == "__main__":
    main()
