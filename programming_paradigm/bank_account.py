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
            self.account_balance -= amount 
            return f"Withdrew: ${amount}.0" 
        else:
            print(f"{amount}, should be less than {self.account_balance}")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}.00")
