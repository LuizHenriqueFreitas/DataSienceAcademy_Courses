# module bank operations
# on this file will happen all the bancary operations

# import client class
from Entities.client import Client

# import base account class and your subclasses
from Entities.account import Account, CurrentAccount, SavingsAcconut

# import personalized exception to nonExistentAccountError
from Utils.exceptions import nonExistentAccountError

# define bank class
class Bank:
    # bank class constructor
    def __init__(self, name: str):
        # set bank name
        self.name = name

        # bank clients dictionary (key: CPF, value: client object)
        self._clients = {}

        # account dictionary (key: account number, value: account object)
        self._accounts = {}

    # add new bank client method
    def add_client(self, name: str, cpf: str) -> Client:
        # check is already exists another client with same CPF
        if cpf in self._clients:
            print("Erro: Client with that CPF already registered")
            return self._clients[cpf]

        # create client object and add to dictionary
        new_client = Client(name, cpf)
        self._clients[cpf] = new_client

        print(f"Client {name} sucess registered!")

        return new_client

    # create an account to a client method
    def creat_account(self, client: Client, type: str) -> Account:
        # new account number will be base on system registered accounts count
        account_number = Account.get_total_accounts() + 1

        # create current account if informed type was "current"
        if type.lower() == 'current':
            new_account = CurrentAccount(account_number, client)

        # create savings account if infotmed type was "savings"
        elif type.lower() == 'savings':
            new_account = SavingsAcconut(account_number, client)

        # if type is not valid
        else:
            print("Invalid Account Type. Choose 'current' or 'savings'.")
            return None

        # add account to accounts dictionary
        self._accounts[account_number] = new_account

        # associate account to client
        client.add_account(new_account)
        print(f"{type} Account, number: {account_number} was created to client: {client.name}.")

        return new_account

    # find account method 
    def find_account(self, account_number: int) -> Account:
        # search account by account number
        
        # try to get account by dictionary
        account = self._accounts.get(account_number)

        # if not found, raise a personalized exception
        if not account:
            raise nonExistentAccountError(account_number)

        return account