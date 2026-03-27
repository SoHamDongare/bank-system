#### BANK SYSTEM ####

## Creating a Account Class ##
class Account:
    def __init__(self,account_number,account_holder_name,balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        
## Creating a Deposite method 
    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Deposited amount must be positive !")
        self.balance += amount
        print(f"Deposited {amount} and new balance is {self.balance}.")
        
## Creating a Withdraw method 
    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("withdrawal amount must be positive !")
        if amount > self.balance:
            raise ValueError("Insufficient funds !")
        self.balance -= amount
        print(f"Withdrew {amount} and new balance is {self.balance}.")

## Creating a get_balance method 
    def get_balance(self):
        return self.balance

## Creating a Account Class ##
class Bank:
    def __init__(self,bank_name):
        self.bank_name = bank_name
        self.accounts ={}
        
## Creating a create_account method 
    def create_account(self,account_number,account_holder_name):
        if account_number in self.accounts:
            raise ValueError("Account number already exists!")
        else:
            new_account = Account(account_number,account_holder_name)
            self.accounts[account_number] = new_account
            print(f"Account created for {account_holder_name} with account number {account_number}.")

## Creating a get_account method 
    def get_account(self,account_number):
        if account_number not in self.accounts:
            raise ValueError("Account not found !")
        return self.accounts[account_number]

### Testing
if __name__ == "__main__":

#   CREATE A BANK 
    bank = Bank("My Bank")
    
#   CREATE ACCOUNTS
    bank.create_account("ACC001","Soham")
    
#   GET ACCOUNT AND TEST
    Soham = bank.get_account("ACC001")
    
    Soham.deposit(10000)
    Soham.withdraw(5000)
    print(f"Soham's Balance:{Soham.get_balance()}")

