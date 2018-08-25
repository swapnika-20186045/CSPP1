'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word

Author: Swapnika
Date: 25-08-2018
'''

import re
def tokenize(string):
    
    str_1 = ""
    for i in string:
        # str_1 = re.sub('[^ A-Za-z0-9]', '', string.lower())
        str_1 = input().split()
    return str_1

def getFrequencyDict(str_1):
    freq = {}
    for x in str_1:
        freq[x] = freq.get(x, 0) + 1
    return freq
      
def main():
    string = input()
    print(tokenize(string))
    getFrequencyDict(str_1)

if __name__ == '__main__':
    main()
