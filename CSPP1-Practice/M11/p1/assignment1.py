'''
Author: Swapnika
Created on 10-08-2018

Exercise: Assignment-1
The first step is to implement some code that allows us to calculate the score
for a single word. The function get_word_score should accept as input a string
of lowercase letters (a word) and return the integer score for that word, using
the game's scoring rules.
'''

def get_word_score(input_word, num_n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    scramble_letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
    'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
    'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
    'y': 4, 'z': 10}
    sc_ore = 0
    for w in input_word:
        sc_ore += scramble_letter_values[w]
    sc_ore *= len(input_word)
    if len(input_word) == num_n:
        sc_ore += 50
    return sc_ore



def main():
    '''
    Main function for the given problem
    '''
    data = input()
    data = data.split()
    print(get_word_score(data[0], int(data[1])))


if __name__ == "__main__":
    main()
