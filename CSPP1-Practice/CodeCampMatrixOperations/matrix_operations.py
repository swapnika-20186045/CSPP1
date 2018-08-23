'''matrix operations'''
def mult_matrix(m_1, m_2, n, m, a, b):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if m == a:
        mul = []
        for i in range(0, n):
            mat = []
            for j in range(0, n):
                sum_val = 0
                for a in range(0, m):
                    sum_val = sum_val + (m_1[i][a] * m_2[a][j])
                mat.append(sum_val)
            mul.append(mat)
        return mul
    print("Error: Matrix shapes invalid for mult")

def add_matrix(m_1, m_2, n, m, a, b):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if n == a and m == b:
        add = []
        for i in range(0, n):
            mat = []
            for j in range(0, m):
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
    n, m = input().split(',')
    m = int(m)
    n = int(n)
    matrix1 = []
    matrix2 = []
    for i in range(0, n):
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
        if count != m:
            flag = False
    if flag != False:
        print("Error: Invalid input for the matrix")

    a, b = input().split(',')
    b = int(b)
    a = int(a)
    for i in range(0, a):
        matrix2.append(list(map(int, input().split())))

    flag = True
    for i in matrix2:
        count = 0
        for j in i:
            count += 1
        if count != b:
            flag = False
    if flag == False:
        print("Error: Invalid input for the matrix")
    if flag == True:
        print(add_matrix(matrix1, matrix2, n, m, a, b))
        print(mult_matrix(matrix1, matrix2, n, m, a, b))

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
