'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word

Author: Swapnika
Date: 25-08-2018
'''

import re
def clean_string(string):
    '''to clean the input string'''
    str_1 = ""

    for _ in string:
        str_1 = re.sub('[^A-Za-z0-9]', '', string.lower())
    # str_1 = string.lower()
    # str_1 = string.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return str_1

def main():
    '''main function'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
