def mult_matrix(m1, m2, n):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    mul = []
    for i in range(0, n):
        mat = []
        for j in range(0, n):
            sum_val = 0
            for k in range(0, n):
                sum_val = sum_val + (m1[i][k] * m2[k][j])
            mat.append(sum_val)
        mul.append(mat)
    return mul

def add_matrix(m1, m2, n):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    add = []
    for i in range(0, n):
        mat = []
        for j in range(0, n):
            mat.append(m1[i][j] + m2[i][j])
        add.append(mat)
    return add

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    n,m = input().split(',')
    n = int(n)
    matrix1 = []
    matrix2 = []
    for i in range(0, n):
        matrix1.append(list(map(int, input().split())))
    n,m = input().split(',')
    n = int(n)
    for i in range(0, n):
        matrix2.append(list(map(int, input().split())))
    print(add_matrix(matrix1, matrix2, n))
    print(mult_matrix(matrix1, matrix2, n))
def main():
    # read matrix 1

    # read matrix 2

    # add matrix 1 and matrix 2
    
    # multiply matrix 1 and matrix 2
    print(read_matrix())
    

if __name__ == '__main__':
    main()
