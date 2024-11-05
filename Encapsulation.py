class BankAccount:
    def __init__(self, initial_balance=0):
        # private attribute for balance
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit: ${amount}")
        else:
            print("Insufficient funds")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdraw: ${amount}")
            else:
                print("Insufficient funds")
        else:
            print("withdrawal amount must be positive")

    def get_balance(self):
        # provide control access to balance
        return self.balance

account = BankAccount(100)
account.deposit(100)
account.withdraw(100)
print(account.get_balance())
account.withdraw(-100)

print(f"Current Balance: ${account.get_balance()}")






