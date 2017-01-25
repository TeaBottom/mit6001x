#  Purpose: Write a program to calculate the credit card balance after one year if a person only pays the minimum
#  monthly payment required by the credit card company each month.

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def remainingBalance(balance, months):
    """
    :param balance: starting credit card balance
    :param months: total months to pay
    :return: remaining balance
    """
    if months == 0:
        return balance  # base of the recursion
    else:
        # calculate new balance
        monthlyInterestRate = annualInterestRate / 12.0
        minMonthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - minMonthlyPayment
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        return remainingBalance(balance, months-1)

print('Remaining balance: ' + str("%.2f" % remainingBalance(balance, 12)))  # print function output w/ rounding
