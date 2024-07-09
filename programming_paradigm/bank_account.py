class BankAccount:
    def __init__(self, account_balance, initial_balance=0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance
    
        
    def deposit(self,amount):
        if amount > 0:
            self.account_balance = amount + self.account_balance
            return f"Deposited: ${amount}.0" 

    def withdraw(self,amount):
        if amount > self.account_balance:
            return ("Insufficient funds.") 
        else:
            return ("Withdrew: {amount}.0")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}.00")
