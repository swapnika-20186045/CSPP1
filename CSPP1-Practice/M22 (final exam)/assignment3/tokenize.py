'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word

Author: Swapnika
Date: 25-08-2018
'''

def tokenize(string):
    
    str_1 = ""
    for i in string:
        # str_1 = re.sub('[^A-Za-z0-9]', '', string.lower())
        str_1 = string.split()
    return str_1
            
def main():
    string = input()
    print(tokenize(string))

if __name__ == '__main__':
    main()
