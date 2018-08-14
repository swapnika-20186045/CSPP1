'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''

def int_cast(card):
    if card[0] = 'T':
        return 10
    elif card[0]= 'J':
        return 11
    elif card[0]= 'Q':
        return 12
    elif card[0]= 'K':
        return 13
    elif card[0]= 'A':
        return 14
    return int(card[0])

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    temp_hand = sorted(hand, key = int_cast) 
    for card_index in range(len(hand)-1):
        if int_cast(temp_hand[card_index+1]) - int_cast(temp_hand[card_index]) != 1:
            return False
    return True

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    # count_diamond = 0
    # count_heart = 0
    # count_spade = 0
    # count_club = 0
    # for i in hand:
    #   if i[1] = 'D':
    #       count_diamond += 1
    #   elif i[1] = 'H':
    #       count_heart += 1
    #   elif i[1] = 'S':
    #       count_spade += 1
    #   elif i[1] = 'C':
    #       count_club += 1
    #   else:
    #       print("invalid suit")
    # if count_diamond == 5 or count_heart == 5 or count_spade == 5 or count_club ==5:
    #   return True
    # return False
    suit = hand[0][1]
    for i in hand:
        if suit != i[1]:
            return False
    return True

def is_straightflush(hand):
    '''check if it is straight flush'''
    if is_straight(hand) and is_flush(hand):
        return True
    return False

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    if poker_rank == is_straightflush(hand):
        return 3 * int_cast(max(hands, key=int_cast))
    elif poker_rank == is_flush(hand):
        return 2 * int_cast(max(hands, key=int_cast))
    elif poker_rank == is_straight(hand):
        return 1 * int_cast(max(hands, key=int_cast))
    return 0

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
