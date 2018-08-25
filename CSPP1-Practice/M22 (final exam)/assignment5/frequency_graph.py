'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph

Author: Swapnika
Date: 25-08-2018
'''

def frequency_graph(dictionary):
    '''print frequency of keys using '#' '''
    keys = sorted(dictionary.keys())
    for key in keys:
        print(key, "-", dictionary[key]*('#'))


def main():
    '''main function'''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
