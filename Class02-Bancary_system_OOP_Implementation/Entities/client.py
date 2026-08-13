# module client entity

""" The "Client class" work's like a template for all clients on
    our applications, each one will has a name, a cpf, and any or N
    accountes related
"""

# define the client class
class Client:

    """ Here's possible to see, at python you declare the class variables
        inside the constructor method, as below
    """
    # class contructor method
    def __init__(self, name: str, cpf:str):

        # set name atribut for the object
        self.name = name

        # set cpf atribut for the object
        self.cpf = cpf

        # set accounts atribut for the objet
        self.accounts = []

    # method to add a new account to client
    def add_account(self, account):
        # insert the account object to accounts client list
        self.accounts.append(account)

    # special method to define object string presentation 
    def __str__(self):
        # return a formated string with client name and cpfs
        return f"Client: {self.nome} (CPF: {self.cpf})"
    