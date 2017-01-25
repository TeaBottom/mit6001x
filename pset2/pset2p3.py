# Use bisection search to calculate the minimum fixed monthly payment needed in order to
# pay off a credit card balance within 12 months

balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0

def minMonthlyPayment(lowerBound, upperBound):
    """

    :param lowerBound: lower bound for bisection search
    :param upperBound: upper bound for bisection search
    :return: minimum fixed monthly payment needed to pay off balance in 12 months
    """

    def remainingBalance(balance, minPay, months): # calculates remaining balance after x months
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
            monthlyUnpaidBalance = balance - minPay
            balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
            return remainingBalance(balance, minPay, months-1)

    minPay = (lowerBound + upperBound) / 2  # new minPay is the average between the lower and upper bounds
    if float('%.2f' % remainingBalance(balance, minPay, 12)) == 0:  # base case minPay pays off the balance
        return minPay  # return out the value for minPay
    elif remainingBalance(balance, minPay, 12) < 0:  # upper bound is too large
        return minMonthlyPayment(lowerBound, minPay)  # new upper bound = current minPay
    else:  # lower bound is too small
        return minMonthlyPayment(minPay, upperBound)  # new lower bound = current minPay
print("Lowest Payment: " + str("%.2f" % minMonthlyPayment(lowerBound, upperBound)))  # display minPay
