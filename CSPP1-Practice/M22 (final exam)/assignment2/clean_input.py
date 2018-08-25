'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.

Author: Swapnika
Date: 25-08-2018
'''

def clean_string(string):
    str_1 = ""
    str_1 = re.sub('[^ A-Za-z0-9]', '', text.lower())
    return str_1

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
