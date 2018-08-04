'''
Author : Swapnika
Created on 4-08-2018
'''

def main():
    '''Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
    example : ab!@#cd is the input, the output is ab   cd
    Output has three spaces, which are to be replaced with these special characters
    '''
    st_r = input()
    sp_ch = ""
    for i in st_r:
        if i in "!#@$%^&*()_+":
            i = " "
        sp_ch = sp_ch + i
    print(sp_ch)

if __name__ == "__main__":
    main()
