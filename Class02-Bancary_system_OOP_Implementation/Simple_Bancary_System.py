# on this file we'll implement the system console menu

# import bank class to controll operations
from Operations.bank import Bank

# import customizes exceptions
from Utils.exceptions import insuficientBalanceError, nonExistentAccountError


# function to show main operations menu
def main_menu():

    print("\n====== Class02 - Simple Bancary System ======\n")
    print("1. Add Client")
    print("2. Creat Account")
    print("3. Access Account")
    print("4. Sair\n")

    # return user selected option
    return input("Choose one option: ")

# functino show especific account operations
def account_menu(bank):
    try:
        # ask user the account number
        account_num = int(input("Type the account number: "))

        # search account on system, can return exception if don't find
        account = bank.find_account(account_num)

        # inside account operations menu
        while True:

            print(f"\n==== Account number: {account._number} options ====")
            print(f"Client: {account._client.name} | Balance: R${account.balance:.2f}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Generate Extract")
            print("4. Back to Main Menu")

            option = input("Choose one option: ")

            if option == '1':
                # make an account deposit
                value = float(input("Type the deposit value: "))
                account.deposit(value)

            elif option == '2':
                # try withdraw
                try:
                    value = float(input("Type withdraw value: "))
                    account.withdraw(value) # polimorphism: depends each account type
                except insuficientBalanceError as e:
                    print(f"Operation error: {e}")

            elif option == '3':
                # show account extract
                account.extract()

            elif option == '4':
                # get out account menu and go back to main menu
                break

            else:
                print("Invalid Option! Try again.")

    except nonExistentAccountError as e:
        print(f"Error: {e}")

def main():
    # instantiate bank obeject
    bank = Bank("Generic Digital Bank")

    # main system loop
    while True:
        
        option = main_menu()

        if option == '1':

            # Add new Client runtime
            name = input("Type the client name: ")
            cpf = str(input("Type the client CPF: "))
            bank.add_client(name, cpf)

        elif option == '2':
            # create new account and link to a client
            cpf = input("Type the client CPF to link account: ")
            client = bank._clients.get(cpf)

            if client:
                type = input("Type the account type (current/savings): ")
                bank.creat_account(client, type)

            else: 
                print("Client not found, please register client before create account")

        elif option == '3':
            # show the account operations menu
            account_menu(bank)

        elif option == '4':
            # ShutDown program
            print("\nThank you for use our system! See you soon :)\n")
            break

        else:
            print("\nInvalid Option! Please try again.\n")

# entrance application point
if __name__ == "__main__":
    main()