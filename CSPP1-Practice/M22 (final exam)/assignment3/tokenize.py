'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word

Author: Swapnika
Date: 25-08-2018
'''

import re
def tokenize(string):
    reg = re.compile('[^ A-Za-z0-9]')
    a_dict = {}
    list_1 = []
    for i in string:
        list_1.append(reg.sub('', i).split())
    for j in list_1:
        for k in j:
            a_dict[k] = a_dict.get(k, 0)+1
    return a_dict
    
def main():
    n = int(input())
    list_strs = []
    for _ in range(n):
        list_strs.append(input())
    print(tokenize(list_strs))

if __name__ == '__main__':
    main()