'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word

Author: Swapnika
Date: 25-08-2018
'''
import re
def word_list(text):
    '''
        Change case to lower and split the words using a SPACE
        Clean up the text by remvoing all the non alphabet characters
        return a list of words
    '''
    str_1 = ""
    list_1 = []
    str_1 = re.sub('[^ a-z]', '', text.lower())
    # str_1 = text.lower()
    list_1 = str_1.split()
    return list_1

def tokenize(string):
    a_dict = {}
    # initialize a search index (an empty dictionary)
    doc_list = list_1
    len_doc_list = len(doc_list)
    for i in range(len_doc_list):
        doc_list[i] = word_list(doc_list[i])
        doc_list[i] = collections.Counter(doc_list[i])
    # iterate through all the string
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop
    for doc_id, doc in enumerate(doc_list):
        for word in doc:
            if word in a_dict:
                a_dict[word].append((doc_id, doc_list[doc_id][word]))
            else:
                a_dict[word] = [(doc_id, doc_list[doc_id][word])]
        # clean up doc and tokenize to words list
        # add or update the words of the doc to the search index
    return a_dict

#     wordlist = string.split()
#     wordfreq = []
#     for i in wordlist:
#         wordfreq.append(wordlist.count(i))
#     return wordfreq
#     # for i in string:
#     #     str_1 = input().split()
#     # return str_1
# def wordListToFreqDict(wordlist):
#     wordfreq = [wordlist.count(p) for p in wordlist]
#     return dict(zip(wordlist,wordfreq))


# # def getFrequencyDict(sequence):
# #     freq = {}
# #     for x in sequence:
# #         freq[x] = freq.get(x, 0) + 1
# #     return freq
      
def main():
    # wordlist = []
    string = input()
    print(tokenize(string))
    # print(wordListToFreqDict(wordlist))
    # getFrequencyDict(str_1)

if __name__ == '__main__':
    main()