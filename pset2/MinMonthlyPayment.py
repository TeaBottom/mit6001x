# Purpose: to calculate the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months

balance = 4773
annualInterestRate = 0.2

def minMonthlyPayment(minPay):
    """

    :param minPay: initial value for the fixed monthly payment to pay off credit card balance
    :return: minimum fixed monthly payment needed to pay off balance in 12 months
    """

    def remainingBalance(balance, minPay, months): # modified from pset2p1
        """
        :param balance: starting credit card balance
        :param minPay: minimum monthly payment
        :param months: total months to pay
        :return: remaining balance
        """
        if months == 0:
            return balance  # base of the recursion
        else:
            # calculate new balance
            monthlyInterestRate = annualInterestRate / 12.0
            monthlyUnpaidBalance = balance - minPay
            balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
            return remainingBalance(balance, minPay, months-1)

    if remainingBalance(balance, minPay, 12) < 0:  # check if minPay/month is enough to pay off balance in 12 months
        return minPay
    else:
        return minMonthlyPayment(minPay+10)  # increases minPay by 10 and repeat function

print("Lowest Payment: " + str(minMonthlyPayment(0)))  # display the min monthly payment
