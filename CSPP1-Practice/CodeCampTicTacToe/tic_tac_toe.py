'''
tic-tac-toe

Author: Swapnika
Date: 24-08-2018
'''
def is_horizontal(main_list, turn):
    '''to check the game horizontally'''
    count = 0
    for lo_op in range(3):
        for in_loop in range(3):
            if turn not in main_list[lo_op][in_loop]:
                count += 1
        if count == 0:
            return True
        count = 0
    return False

def is_vertical(main_list, turn):
    '''to check the game vertically'''
    count = 0
    for lo_op in range(3):
        for in_loop in range(3):
            if turn not in main_list[in_loop][lo_op]:
                count += 1
        if count == 0:
            return True
        count = 0
    return False

def is_diagonal_forward(main_list, turn):
    '''to check forward diagonal in the game'''
    count = 0
    for lo_op in range(3):
        if turn not in main_list[lo_op][lo_op]:
            count += 1
    if count == 0:
        return True
    return False

def is_diagonal_backward(main_list, turn):
    '''to check backward diagonal in the game'''
    count = 0
    in_loop = 2
    for lo_op in range(3):
        if turn not in main_list[lo_op][in_loop]:
            count += 1
        in_loop -= 1
    if count == 0:
        return True
    return False

def read_input():
    '''to read the input'''
    list_1 = []
    for _ in range(3):
        list_1.append(list(map(str, input().split())))
    return list_1

def main():
    '''main function'''
    count = 0
    x_count = 0
    o_count = 0
    char_count = 0
    other_char = 0
    main_list = read_input()

    for lo_op in range(3):
        for in_loop in range(3):
            if main_list[lo_op][in_loop] == 'x':
                x_count += 1
            elif main_list[lo_op][in_loop] == 'o':
                o_count += 1
            elif main_list[lo_op][in_loop] == '.':
                char_count += 1
            else:
                other_char += 1
    if other_char != 0:
        print("invalid input")
        count += 1
    elif x_count > o_count + 1 or o_count > x_count + 1:
        print("invalid game")
        count += 1

    turn_x = 'x'
    boolean_x = (is_horizontal(main_list, turn_x)
                 or is_vertical(main_list, turn_x)
                 or is_diagonal_forward(main_list, turn_x)
                 or is_diagonal_backward(main_list, turn_x))

    turn_o = 'o'
    boolean_o = (is_horizontal(main_list, turn_o)
                 or is_vertical(main_list, turn_o)
                 or is_diagonal_forward(main_list, turn_o)
                 or is_diagonal_backward(main_list, turn_o))

    if boolean_x and boolean_o and count == 0:
        print("invalid game")
        count += 1
    if boolean_x and count == 0:
        print(turn_x)
        count += 1
    if boolean_o and count == 0:
        print(turn_o)
        count += 1
    if count == 0:
        print("draw")

if __name__ == '__main__':
    main()
