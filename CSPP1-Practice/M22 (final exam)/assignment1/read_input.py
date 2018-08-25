'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def read_input():
    str_1 = ""
    n = int(input())

    for i in range(n):
        str_1 += input()
        i += 1
    print(str_1)
    # return list_1

def main():
    read_input()
    # return l_1

if __name__ == '__main__':
    main()
