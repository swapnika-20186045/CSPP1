'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word

Author: Swapnika
Date: 25-08-2018
'''
# def getFrequencyDict(l_l):
#     """
#     Returns a dictionary where the keys are elements of the sequence
#     and the values are integer counts, for the number of times that
#     an element is repeated in the sequence.

#     sequence: string or list
#     return: dictionary
#     """
#     # freqs: dictionary (element_type -> int)
#     freq = {}
#     for x in l_l:
#         freq[x] = freq.get(x, 0) + 1
#     return freq

def clean_input(da_ta):
    for i in range(int(num_n)):
        da_ta = input()
        l_l = da_ta.split()
        i += 1
    return l_l

def main():
    '''main function'''
    num_n = input()
    # a_dict = {}
    # for i in range(int(num_n)):
    #     da_ta = input()
    #     l_l = da_ta.split()
    #     i += 1
    # data_1 = input()
    print(clean_input(da_ta))
