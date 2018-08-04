'''

Author:Swapnika
Created on 2-8-2018

'''


def main():
    '''
    function is used to count number of vowels
    '''
    st_r = input()
    coun_t = 0
    for cha_r in st_r:
        if cha_r in ('a', 'e', 'i', 'o', 'u'):
            coun_t += 1
    print(coun_t)

if __name__ == "__main__":
    main()
