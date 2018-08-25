'''
Write a python program to read multiple lines of text input and store the input into a string.

Author: Swapnika
Date: 25-08-2018
'''

def read_input():
    '''to read input'''
    str_1 = ""
    num_n = int(input())

    for _ in range(num_n):
        str_1 += input() + '\n'
    print(str_1)
    # return list_1

def main():
    '''main function'''
    read_input()

if __name__ == '__main__':
    main()
