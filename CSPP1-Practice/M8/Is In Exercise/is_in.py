'''
Author:Swapnika
Created on 06-08-2018
'''
# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments 
#a character and String and returns the isIn(char, aStr) which retuns a boolean value.
# This function takes in two arguments character and String and returns
#one boolean value.

def isIn_2(char,aStr):
    sorted_aStr = sorted(aStr)
    x = isIn(0,len(sorted_aStr),char,sorted_aStr)
    return x

def isIn(minimum,maximum,char,aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    mid = (minimum+maximum)//2
    if aStr[mid] == char:
        return "True"
    elif mid == minimum or mid == maximum:
        return "False"
    else:
        if aStr[mid] > char:
            return isIn(minimum,mid,char,aStr)
        elif aStr[mid] < char:
            return isIn(mid,maximum,char,aStr)

def main():
    data = input()
    data = data.split()
    print(isIn_2(data[0], data[1]))


if __name__ == "__main__":
    main()