'''
Author:Swapnika
Created on 2-8-2018
'''

def main():
    '''longest alphabetical sequence in given string'''
    s_1 = input()
    s1 = ''
    fs = ''
    n = len(s_1)
    f_max = 0
    f_cnt = 0
    fs = s_1[0]
    for i in range(0, n-1):
        if ord(s_1[i]) <= ord(s_1[i+1]):
            f_cnt += 1
            fs = fs + s_1[i+1]
        else:
            if f_cnt > f_max:
                f_max = f_cnt
                s1 = fs
            f_cnt = 0
            fs = s_1[i+1]
    if f_cnt > f_max:
        s1 = fs
    print(s1)
if __name__== "__main__":
    main()
