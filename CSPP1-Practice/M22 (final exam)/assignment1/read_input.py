'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def read_input():
    list_1 = []
    # n = len(input())

    for _ in range(3):
        list_1.append(input() + '\n')
    return list_1

def main():
    l_1 = read_input()

if __name__ == '__main__':
    main()