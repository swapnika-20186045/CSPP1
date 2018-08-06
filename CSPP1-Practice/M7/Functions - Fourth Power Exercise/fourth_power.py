'''
Author:Swapnika
Created on 06-08-2018
'''

def square(x):
    '''
    x: int or float.
    Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power.

    '''
    return x**2
    


def fourthPower(x):
    '''
    x: int or float.
    Write a Python function, fourthPower, that takes in one number and returns that value raised to the fourth power.
    '''
    return square(square(x))
   

def main():
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if(temp[1] == '0'):
        print(fourthPower(int(float(str(data)))))
    else:
        print(fourthPower(data))

if __name__ == "__main__":
    main()
