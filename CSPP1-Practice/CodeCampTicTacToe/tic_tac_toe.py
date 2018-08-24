def is_horizontal(main_list, turn):
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
    count = 0
    for in_loop in range(3):
        for lo_op in range(3):
            if turn not in main_list[in_loop][lo_op]:
                count += 1
        if count == 0:
            return True
        count = 0
    return False

def is_diagonal_forward(main_list, turn):
    count = 0
    for lo_op in range(3):
        if turn not in main_list[lo_op][lo_op]:
            count += 1
    if count == 0:
            return True
        count = 0
    return False                    

def is_diagonal_backward(main_list, turn):
    '''Checks for diagnol backward match'''
    count = 0
    in_loop = 2
    for lo_op in range(3):
        if turn not in main_list[lo_op][in_loop]:
            count += 1
        in_loop -= 1
    if count == 0:
        return True
    return False

def main():
    '''main function'''
    count = 0
    x_count = 0
    o_count = 0
    char_count = 0
    other_char = 0
    main_list = []
    for i in range(3):
        main_list.append(list(map(str, input().split())))

    turn_x = 'x'
    boolean_x = (is_horizontal(main_list, turn_x)
                 or is_vertical(main_list, turn_x)
                 or is_diagonal_forward(main_list, turn_x)
                 or is_diagonal_backward(main_list, turn_x))

    turn_o = 'o'
    boolean_o = (is_horizontal(main_list, turn_o)
                 or is_vertical(main_list, turn_o)
                 or is_diagnol_forward(main_list, turn_o)
                 or is_diagnol_backward(main_list, turn_o))

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
