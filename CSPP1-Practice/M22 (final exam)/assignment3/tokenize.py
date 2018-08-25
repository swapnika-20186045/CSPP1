'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word

Author: Swapnika
Date: 25-08-2018
'''

def tokenize(string):
    words = string.split()
    a_dict = {}
    for i in words:
        if i in a_dict:
            a_dict[i] += 1
        else:
            a_dict[i] = 1
    return a_dict
    
def main():
    n = int(input)
    text = ''
    for _ in range(n):
        text = input()+"\n"
    print(tokenize(text))

if __name__ == '__main__':
    main()