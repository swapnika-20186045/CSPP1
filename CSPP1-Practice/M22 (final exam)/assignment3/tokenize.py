'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word

Author: Swapnika
Date: 25-08-2018
'''
import re
def tokenize(string):
    wordlist = string.split()
    wordfreq = []
    for i in wordlist:
        wordfreq.append(wordlist.count(i))
    return wordfreq
    # for i in string:
    #     str_1 = input().split()
    # return str_1
def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    return dict(zip(wordlist,wordfreq))


# def getFrequencyDict(sequence):
#     freq = {}
#     for x in sequence:
#         freq[x] = freq.get(x, 0) + 1
#     return freq
      
def main():
    wordlist = []
    string = input()
    print(tokenize(string))
    print(wordListToFreqDict(wordlist))
    # getFrequencyDict(str_1)

if __name__ == '__main__':
    main()