'''
Author:Swapnika
Created on 2-8-2018
'''

def main():
    '''longest alphabetical sequence in given string'''
    st_r = input()
    s_1 = ''
    f_s = ''
    n = len(st_r)
    f_max = 0
    f_cnt = 0
    f_s = st_r[0]
    for i in range(0, n-1):
        if ord(st_r[i]) <= ord(st_r[i+1]):
            f_cnt += 1
            f_s = f_s + st_r[i+1]
        else:
            if f_cnt > f_max:
                f_max = f_cnt
                s_1 = f_s
            f_cnt = 0
            f_s = st_r[i+1]
    if f_cnt > f_max:
        s_1 = f_s
    print(s_1)
if __name__ == "__main__":
    main()
