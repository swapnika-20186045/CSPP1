'''
Author:Swapnika
Created on 2-8-2018
'''

def main():
    '''
    number of times a small string occurs
    '''
    st_r = input()
    coun_t = 0
    for i in range(0, len(st_r)-2):
        if (st_r[i] == 'b' and st_r[i+1] == 'o' and st_r[i+2] == 'b'):
            coun_t += 1
    print(coun_t)

if __name__ == "__main__":
    main()
