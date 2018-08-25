'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word

Author: Swapnika
Date: 25-08-2018
'''

def tokenize(string):
    string = input()
    str_1 = ""
    for i in string:
        str_1 = input().split()
    return str_1
            
def main():
    print(tokenize(string))

if __name__ == '__main__':
    main()
