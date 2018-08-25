'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.

Author: Swapnika
Date: 25-08-2018
'''

def print_dictionary(dictionary):
    keys = sorted(dictionary.keys())
    for key in keys:
        print(key, " - ", dictionary[key])

def main():
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
