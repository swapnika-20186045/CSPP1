'''matrix operations'''
def mult_matrix(m_1, m_2, rows_1, columns_1, rows_2, columns_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if columns_1 == rows_2:
        mul = []
        for i in range(0, rows_1):
            mat = []
            for j in range(0, rows_1):
                sum_val = 0
                for k in range(0, columns_1):
                    sum_val = sum_val + (m_1[i][k] * m_2[k][j])
                mat.append(sum_val)
            mul.append(mat)
        return mul
    print("Error: Matrix shapes invalid for mult")

def add_matrix(m_1, m_2, rows_1, columns_1, rows_2, columns_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if rows_1 == rows_2 and columns_1 == columns_2:
        add = []
        for i in range(0, rows_1):
            mat = []
            for j in range(0, columns_1):
                mat.append(m_1[i][j] + m_2[i][j])
            add.append(mat)
        return add
    print("Error: Matrix shapes invalid for addition")

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    rows_1, columns_1 = input().split(',')
    columns_1 = int(columns_1)
    rows_1 = int(rows_1)
    matrix1 = []
    matrix2 = []
    for i in range(0, rows_1):
        matrix1.append(list(map(int, input().split())))
    # print(matrix1)
    # n,m = input().split(',')
    # n = int(n)
    # for i in range(0, n):
    #     matrix2.append(list(map(int,input().split())))

    flag = True
    for i in matrix1:
        count = 0
        for _ in i:
            count += 1
        if count != columns_1:
            flag = False
    if flag is not True:
        print("Error: Invalid input for the matrix")

    rows_2, columns_2 = input().split(',')
    columns_2 = int(columns_2)
    rows_2 = int(rows_2)
    for i in range(0, rows_2):
        matrix2.append(list(map(int, input().split())))

    flag = True
    for i in matrix2:
        count = 0
        for _ in i:
            count += 1
        if count != columns_2:
            flag = False
    if flag is not True: 
        print("Error: Invalid input for the matrix")
    if flag is True:
        print(add_matrix(matrix1, matrix2, rows_1, columns_1, rows_2, columns_2))
        print(mult_matrix(matrix1, matrix2, rows_1, columns_1, rows_2, columns_2))

def main():
    '''main function'''
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    read_matrix()
    # print(add_matrix())
    # print(mult_matrix())

if __name__ == '__main__':
    main()
