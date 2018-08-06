'''
Author:Swapnika
Created on 06-08-2018
'''


def square(x):
    '''
    x: int or float.
    write a Python function, square, that takes in one number and returns the square of that number.
    '''
    return x**2
    
# Correct

def main():
	data = input()
	data = float(data)
	temp = str(data).split('.')
	if(temp[1] == '0'):
		print(square(int(float(str(data)))))
	else:
		print(square(data))

if __name__== "__main__":
	main()

