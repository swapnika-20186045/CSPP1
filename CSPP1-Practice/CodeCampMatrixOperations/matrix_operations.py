'''matrix operations'''
def mult_matrix(m1, m2, n_1, m_1, n_2, m_2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if m_1 == n_2:
        mul = []
        for i in range(0, n_1):
            mat = []
            for j in range(0, n_1):
                sum_val = 0
                for n_2 in range(0, m_1):
                    sum_val = sum_val + (m1[i][n_2] * m2[n_2][j])
                mat.append(sum_val)
            mul.append(mat)
        return mul
    else:
        print("Error: Matrix shapes invalid for mult")

def add_matrix(m1, m2, n_1, m_1, n_2, m_2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if n_1 == n_2 and m_1 == m_2:
        add = []
        for i in range(0, n_1):
            mat = []
            for j in range(0, m_1):
                mat.append(m1[i][j] + m2[i][j])
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
    n_1, m_1 = input().split(',')
    m_1 = int(m_1)
    n_1 = int(n_1)
    matrix1 = []
    matrix2 = []
    for i in range(0, n_1):
        matrix1.append(list(map(int, input().split())))
    # print(matrix1)
    # n,m = input().split(',')
    # n = int(n)
    # for i in range(0, n):
    #     matrix2.append(list(map(int,input().split())))

    flag = True
    for i in matrix1:
        count = 0
        for j in i:
            count += 1
        if count != m_1:
            flag = False
    if flag == False:
        print("Error: Invalid input for the matrix")

    n_2, m_2 = input().split(',')
    m_2 = int(m_2)
    n_2 = int(n_2)
    for i in range(0, n_2):
        matrix2.append(list(map(int, input().split())))

    flag = True
    for i in matrix2:
        count = 0
        for j in i:
            count += 1
        if count != m_2:
            flag = False
    if flag == False:
        print("Error: Invalid input for the matrix")
    if flag == True:
        print(add_matrix(matrix1, matrix2, n_1, m_1, n_2, m_2))
        print(mult_matrix(matrix1, matrix2, n_1, m_1, n_2, m_2))

def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    read_matrix()
    # print(add_matrix())
    # print(mult_matrix())

if __name__ == '__main__':
    main()
