'''
Author:Swapnika
Created on 06-08-2018
'''

def iter_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    res = 1
    for _ in range(exp):
        res = res * base
    return res

def main():
    '''main function'''
    data = input()
    data = data.split()
    print(iter_power(float(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
