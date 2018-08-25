'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''
import re
def frequency_graph(dictionary):
    keys = sorted(dictionary.keys())
    for key in keys:
        str_1 = (key, "-", dictionary[key])
        str_2 = re.sub('[^A-Za-z]', '#', str_1.lower())
    print(str_2)


def main():
    str_1 = ''
    str_2 = ''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
