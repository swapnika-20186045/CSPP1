'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''

def is_straight(hand):
    '''
     straight function
    '''
    stng_values = "--23456789TJQKA"
    hand_values = []
    for i in hand:
        hand_values.append(stng_values.index(i[0]))
    hand_values.sort()
    for i in range(len(hand_values) - 1):
        if hand_values[i] - hand_values[i+1] != -1:
            return False
    return True

def is_flush(hand):
    '''
      Flush function
    '''
    values_set = set({})
    for i in hand:
        values_set.add(i[1])
    return len(values_set) == 1

def is_four(hand):
    '''
    four of a kind function
    '''
    hand_values = [f_1 for f_1, s in hand]
    set_val = set(hand_values)
    if len(set_val) != 2:
        return False
    for f_1 in set_val:
        if hand_values.count(f_1) == 4:
            return True
    return False

def is_three(hand):
    '''
    three of a kind
    '''
    hand_values = [f_1 for f_1, s in hand]
    set_val = set(hand_values)
    if len(set_val) <= 2:
        return False
    for f_1 in set_val:
        if hand_values.count(f_1) == 3:
            return True
    return False

def is_onepair(hand):
    '''
    one of a kind function
    '''
    hand_values = [f_1 for f_1, s in hand]
    set_val = set(hand_values)
    twopairs = [f_1 for f_1 in set_val if hand_values.count(f_1) == 2]
    if len(twopairs) != 1:
        return False
    return True

def is_full(hand):
    '''
    full hand function
    '''
    hand_values = [f_1 for f_1, s in hand]
    set_val = set(hand_values)
    if len(set_val) != 2:
        return False
    for f_1 in set_val:
        if hand_values.count(f_1) == 3:
            return True
    return False

def is_twopair(hand):
    '''
    two of a kind function
    '''
    hand_values = [f_1 for f_1, s in hand]
    set_val = set(hand_values)
    twopairs = [f_1 for f_1 in set_val if hand_values.count(f_1) == 2]
    if len(twopairs) != 2:
        return False
    return True

def hand_rank(hand):
    '''
    hand rank function
    '''
    rank_value = 0
    if is_straight(hand) and is_flush(hand):
        rank_value = 8
    elif is_flush(hand):
        rank_value = 7
    elif is_straight(hand):
        rank_value = 6
    elif is_four(hand):
        rank_value = 5
    elif is_three(hand):
        rank_value = 4
    elif is_onepair(hand):
        rank_value = 3
    elif is_full(hand):
        rank_value = 2
    elif is_twopair(hand):
        rank_value = 1
    else:
        rank_value = 0
    return rank_value

def poker(hands):
    '''
    poker function
    '''
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HAND = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HAND.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HAND)))
