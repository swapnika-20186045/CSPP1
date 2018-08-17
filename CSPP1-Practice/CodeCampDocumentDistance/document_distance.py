'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math
import copy

def similarity(common_dict):
    '''
        Compute the document distance as given in the PDF
    '''
    num_val = 0
    den_1 = 0
    den_2 = 0
    distance = 0
    for i in common_dict:
        num_val += common_dict[i][0] * common_dict[i][1]
        den_1 += common_dict[i][0] ** 2
        den_2 += common_dict[i][1] ** 2
    #print(num_val,den_1,den_2)
    distance = (num_val) / (math.sqrt(den_1) * math.sqrt(den_2))
    return distance

def load_stopwords(file_name):
    '''
        loads stop words from a file and returns a dictionary
    '''
    # file_name = "stopwords.txt"
    stopwords = {}
    with open(file_name, 'r') as file_name:
        for line in file_name:
            stopwords[line.strip()] = 0
    return stopwords

def word_list(input1, input2):
    '''making a wordlist'''
    list_1 = []
    list_2 = []
    key_list = []
    str_1 = ""
    str_2 = ""

    str_1 = re.sub('[^ a-z]', '', input1.lower())
    str_2 = re.sub('[^ a-z]', '', input2.lower())
    # print(str_1,str_2)

    list_1 = str_1.split(" ")
    list_2 = str_2.split(" ")
    # print(list_1,list_2)
    stopwords = load_stopwords("stopwords.txt")
    key_list = list(stopwords.keys())

    word_list1 = list_1[:]
    for i in word_list1:
        if i in key_list:
            list_1.remove(i)

    word_list2 = list_2[:]
    for i in word_list2:
        if i in key_list:
            list_2.remove(i)
    #print(list_1,list_2)
    return freq_count(list_1, list_2)

def freq_count(list_1, list_2):
    '''frequency count in dictionaries'''
    freq_dict1 = {}
    freq_dict2 = {}
    common_dict = {}

    for k in list_1:
        if k not in freq_dict1:
            freq_dict1[k] = 1
        else:
            freq_dict1[k] += 1

    for k in list_2:
        if k not in freq_dict2:
            freq_dict2[k] = 1
        else:
            freq_dict2[k] += 1

    for i in freq_dict1:
        if i in freq_dict2:
            common_dict[i] = [freq_dict1[i], freq_dict2[i]]
        else:
            common_dict[i] = [freq_dict1[i], 0]

    for p_1 in freq_dict2:
        if p_1 not in common_dict:
            common_dict[p_1] = [0, freq_dict2[p_1]]

    d_1 = copy.deepcopy(common_dict)
    for h_1 in d_1:
        length_l = len(h_1)
        if length_l == 0:
            del common_dict[h_1]
    #print(common_dict)
    return common_dict

# def function():
#     '''stopwords'''
#     file_name = load_stopwords("stopwords.txt")

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    #print(input1,input2)

    common_dict_1 = word_list(input1, input2)
    print(similarity(common_dict_1))

if __name__ == '__main__':
    main()
