class BankAccount:
    def __init__(self, account_balance, initial_balance=0):
        self.account_balance = account_balance
        self.initial_balance = initial_balance
    
        
    def deposit(self,amount):
        if amount > 0:
            self.account_balance = amount + self.account_balance
            return self.account_balance
        else:
            print(f"{amount}, should be greater than {self.initial_balance}")

    def withdraw(self,amount):
        if amount > self.account_balance:
            self.account_balance -= amount
            return f"Withdrew: {amount}"
        else:
            print(f"{amount}, should be less than {self.account_balance}")

    def display_balance(self):
        print(f"Current Balance: {self.account_balance}")