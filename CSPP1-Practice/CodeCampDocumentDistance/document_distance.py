'''
    Document Distance - A detailed description is given in the PDF
'''
import re
import math

def similarity(common_dict, dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    num_val = 0
    den_1 = 0
    den_2 = 0
    for i in common_dict:
        num_val += common_dict[i][0] * common_dict[i][1]
    for j in dict1:
        den_1 += dict1[j] ** 2
    for k in dict2:
        den_2 += dict2[k] ** 2

    distance = (num_val) / math.sqrt(den_1*den_2)
    return distance
def word_list(input1, input2):
    list_1 = []
    list_2 = []
    key_list = []
    a = ""
    b = ""

    a = re.sub('[^A-Za-z0-9]',' ', input1.lower())
    b = re.sub('[^A-Za-z0-9]',' ', input2.lower())
    
    list_1 = a.split(" ")
    list_2 = b.split(" ")

    stopwords = load_stopwords("stopwords.txt")
    key_list = stopwords.keys()

    for i in key_list:
        for j in list_1:
            if i == j:
                list_1.remove(j)

    for i in key_list:
        for j in list_2:
            if i == j:
                list_2.remove(j)
    return freq_count(list_1, list_2)

    # return list_1,list_2

def freq_count(list_1, list_2):
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
    # print(freq_dict1, freq_dict2)

    for i in freq_dict1:
        if i in freq_dict2:
            common_dict[i] = [freq_dict1[i], freq_dict2[i]]
        else:
            common_dict[i] = [freq_dict1[i], 0]
    for p in common_dict:
        if p not in common_dict:
            common_dict[p] = [0, freq_dict2[p]]
    return (common_dict, freq_dict1, freq_dict2)

def load_stopwords(file_name):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(file_name, 'r') as file_name:
        for line in file_name:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    (common_dict, dict_1, dict_2) = word_list(input1, input2)
    print(similarity(common_dict, dict_1, dict_2))

if __name__ == '__main__':
    main()
