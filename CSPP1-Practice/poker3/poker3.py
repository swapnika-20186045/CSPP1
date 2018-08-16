'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''

def hand_values(hand):
    '''values'''
    return sorted((["--23456789TJQKA".index(c) for c,x in hand]), reverse = True)

def is_straight(ranks):
    '''
     straight function
    '''
    return (max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5) or (ranks[0:5] == [5, 4, 3, 2] and ranks[0] == 14)

def kind(ranks, n):
    '''which kind'''
    for i in ranks:
        ranks.count(i) == n
        return i

def is_two_pair(ranks):
    '''two pair function'''
    high_val = kind(rank,2)
    low_val = sorted(kind(rank,2))
    if high_val != low_val:
        return high_val, low_val

def is_flush(hand):
    '''
      Flush function
    '''
    value_set = set()
    for i in hand:
        value_set.add(i[1])
    return len(value_set) == 1

def hand_rank(hand):
    '''
    hand rank function
    '''
    rank = hand_values(hand)
    if is_straight(hand) and is_flush(hand):
        return 8, (rank)
    if kind(rank, 4):
        return 7, kind(rank, 4), rank
    if kind(rank, 3) and kind(rank, 2):
        return 6, kind(rank, 3), kind(rank, 2), rank
    if is_flush(hand):
        return 5, rank
    if is_straight(rank):
        return 4, rank
    if kind(rank, 3):
        return 3, kind(rank, 3), rank
    if is_twopair(rank):
        return 2, is_two_pair(rank), rank
    if kind(rank,2):
        return 1, kind(rank,2), rank
    return 0, rank

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
