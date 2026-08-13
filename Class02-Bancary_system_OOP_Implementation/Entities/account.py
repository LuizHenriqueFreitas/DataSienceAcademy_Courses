# module account entity

""" That script will define diferent types od bancary accounts:
    - abstract acconunt made a base to the others;
    - current account;
    - savings account;
"""

""" We also need import some python lib resources, 
    to make this a serius exercise.

    Each one is self explained, why was imported
"""

# import the base abstract class and the abstract methods decorator
from abc import ABC, abstractmethod

# import datetime class to register transactions time stemp
from datetime import datetime

# import personalized exception to insuficient balance
# thats is also a external import, not an internal python lib import
from Utils.exceptions import insuficientBalanceError

# Define the Account abstract class, serves as base to another classes
# That also will serves like an inheritance and encapsulation exemple
class Account(ABC):

    # class atribut to calculate how many accounts was created
    _total_accounts = 0

    # class constructor
    def __init__(self, number: int, client):
        # account number (protected information)
        self._number = number

        # account balance - started with 0.0 (protected information)
        self._balance = 0.0

        # client account owner reference
        self._client = client

        # transactions history list storage
        self._history = []

        # increment the total created account counter
        Account._total_accounts += 1

    # property to acess balaced on a controlled way
    @property
    def balance(self):
        # balance getter allowing controlled access
        return self._balance
    

    # class method to consult the total accounts amount
    @classmethod
    def get_total_accounts(cls):
        # classe method to get total accounts amount
        return cls._total_accounts

    # method to realize deposits
    def deposit(self, value: float):
        # add a value to account balance
        if value > 0:
            
            # increment balance
            self._balance += value

            # registry the transaction time stamp
            # we're using BRL cash, Brazilian cash on this exercise too
            self._history.append((datetime.now(), f"Deposit of R${value:.2f}"))
            print(f"Deposit of R${value:.2f} sucess realized.")

        else:
            print("Invalid Deposit Value!")

    # abstract method - should be implemented by each subclass
    @abstractmethod
    def withdraw(self, value: float):
            """ Logic should be implemented just inside sub class for each necessities"""
            pass

    # show account extract method
    def extract(self):

        # ======== show account extract ========
        print(f"\n--- Account N: {self._number} Extract ---")
        print(f"Client: {self._client.name}")
        print(f"Current Balance: {self._balance:.2f}")
        print(f"Transactions History:")

        # if there's no registred transactions
        if not self._history:
            print("No one transaction registered.")

        # run complete hitory list and show each one
        for data, transaction in self._history:
            print(f"- {data.strftime('%d/%m/%Y %H:%M:%S')}: {transaction}")
        print("------------------------------------------\n")


""" Below there'll be the subclasses delcaration, first one is "CurrenteAccount"
    class, look, the inheritance in python is apllied by <className>(<superClass>).

    Generic information stays on super class;
    Specific information stays on sub class;
"""

# define Current Account subclass
class CurrentAccount(Account): 
    """ This subclass represent a current account
        It's also a polimorphsm exemple
    """

    # i don't know if "cheque especial" is translated to "special check" 1 by 1 like that 

    # defaut constructor with special check limit 
    def __init__(self, number: int, client, limit: float = 500.0):
        # call the base class constructor
        super().__init__(number, client)

        # define special check limit 
        self.limit = limit

    # implements withdraw method with special check
    def withdraw(self, value: float):
        #Allow withdraws using account balance + special check limit

        if value <= 0:
            print("Withdraw Value Ivalid!")
            return

        # calculate available balance (balance + limit)
        available_balance = self._balance + self.limit

        # if the withdraw value overtake the balance available
        if value > available_balance:
            raise insuficientBalanceError(available_balance, value, "Balance and Limit unsuficients.")

        # deducts withdraw value from balance
        self._balance -= value

        # register the transaction on the history
        self._history.append((datetime.now(), f"Withdraw of R${value:.2f}"))
        print(f"Withdraw of R${value:.2f} sucefull realized.")

# define savings account subclass
class SavingsAcconut(Account):
    # call super class contructor
    def __init__(self, number: int, client):
        super.__init__(number, client)

    # implement withdraw method just with available balance
    def withdraw(self, value: float):
        # allow withdraw just if there's suficient balance 
        if value <= 0:
            print("Withdraw Value Invalid.")
            return
        
        # check if there`s suficient balance
        if value > self._balance:
            raise insuficientBalanceError(self._balance, value)

        # deduct balance value
        self._balance -= value

        # register transaction on the history
        self._history.append((datetime.now(), f"Withdraw of R${value:.2f}"))
        print(f"Withdraw of R${value:.2f} sucefull realized.")