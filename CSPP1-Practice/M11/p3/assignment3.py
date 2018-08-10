'''
Author: Swapnika
Created on 09-08-2018
'''
# Assignment-3

#At this point, we have written code to generate a random hand and display that
#hand to the user. We can also ask the user for a word (Python's input) and
#score the word (using your getWordScore). However, at this point we have not
#written any code to verify that a word given by a player obeys the rules
#of the game. A valid word is in the word list; and it is composed entirely of
#letters from the current hand. Implement the isValidWord function.

#Testing: Make sure the test_isValidWord tests pass. In addition, you will want
#to test your implementation by calling it multiple times on the same hand-
#what should the correct behavior be? Additionally, the empty string ('') is
#not a valid word - if you code this function correctly, you shouldn't need an
#additional check for this condition.

#Fill in the code for isValidWord in ps4a.py and be sure you've passed the
#appropriate tests in test_ps4a.py before pasting your function definition here.

def isValidWord(wo_rd, ha_nd, word_list):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    co_unt = 0
    length_word =len(wo_rd)
    for letter_i in wo_rd:
        if letter_i in ha_nd:
            co_unt += 1
    if length_word == co_unt:
        if wo_rd in word_list:
            return True
        else:
            return False
    else:
        return False
    

def main():
    '''main function'''
    word = input()
    num_n = int(input())
    a_dict = {}
    for i in range(num_n):
        data = input()
        length_word = data.split()
        a_dict[length_word[0]] = int(length_word[1])
    l_2 = input().split()
    print(is_validword(wo_rd,a_dict,l_2))
        
if __name__ == "__main__":
    main()
