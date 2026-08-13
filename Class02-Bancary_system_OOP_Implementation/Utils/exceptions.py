# app exceptions module

# define insuficientBalance exception to withdraw operations
class insuficientBalanceError(Exception):
    # exception constructor
    def __init__(self, actual_balance, withdraw_value, message="Insuficient balance to finish this operation."):
        # actual balance at error occured
        self.actual_balance = actual_balance

        # odered value to withdraw
        self.withdraw_value = withdraw_value

        # detalhed error message
        self.message = f"{message} Actual balance: {actual_balance:.2f}, Try to withdraw: {withdraw_value:.2f}"

        # call superclass constructor
        super.__init__(self.message)


# define non exitent account exepction to find account operations
class nonExistentAccountError(Exception):
    # constructor method
    def __init__(self, account_number, message="That specific account was not found."):
        # findless account number
        self.account_number = account_number

        # detalhed error message
        self.message = f"{message} Account Number: {account_number}"

        # call superclass constructor
        super.__init__(self.message)