'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    keys = sorted(dictionary.keys())
    for key in keys:
        if key is digit():
        	keys.replace(key, "#")
    print(key, "-", dictionary[key])


def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
