'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def read_input():
    list_1 = []
    n = int(input())

    for i in range(n):
        list_1.append(input())
        i += 1
    print(list_1)
    # return list_1

def main():
    read_input()
    # return l_1

if __name__ == '__main__':
    main()
