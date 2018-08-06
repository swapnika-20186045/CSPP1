'''
Author:Swapnika
Created on 06-08-2018
'''


def payingdebt_offinayear(bal_ance, annual_interestrate, monthly_paymentrate):
    '''Write a program to calculate the credit card balance after one year if a person only
    pays the minimum monthly payment required by the credit card company each month'''

    i = 1
    balance_copy = bal_ance
    while i <= 12:
        mir = (annual_interestrate) / 12.0
        mmp = (monthly_paymentrate)*(balance_copy)
        mub = (balance_copy) - (mmp)
        balance_copy = (mub) + (mir*mub)
        i += 1
    return "Remaining balance:" + str(round(balance_copy, 2))

def main():
    '''The following variables contain values as described below:
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    monthlyPaymentRate - minimum monthly payment rate as a decimal
    For each month, calculate statements on the monthly payment and remaining balance
    At the end of 12 months, print out the remaining
    balance. Be sure to print out no more than two decimal digits of accuracy - so print'''

    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(payingdebt_offinayear(data[0], data[1], data[2]))

if __name__ == "__main__":
    main()
