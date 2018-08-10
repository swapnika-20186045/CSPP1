'''
Author: Swapnika
Created on 10-08-2018
'''
#Exercise: Assignment-2
#Implement the updateHand function. Make sure this function has no side effects:
#i.e., it must not mutate the hand passed in. Before pasting your function
#definition here, be sure you've passed the appropriate tests in test_ps4a.py.

def update_hand(given_hand, given_word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """

    for wo_rd in given_word:
        if wo_rd in given_hand:
            given_hand[wo_rd] -= 1
    return given_hand

def main():
    '''main function'''
    num_n = input()
    a_dict = {}
    for i in range(int(num_n)):
        da_ta = input()
        l_l = da_ta.split()
        a_dict[l_l[0]] = int(l_l[1])
        i += 1
    data_1 = input()
    print(update_hand(a_dict, data_1))

if __name__ == "__main__":
    main()
