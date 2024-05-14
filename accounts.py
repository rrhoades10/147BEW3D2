from bank import BankAccount


# savings accounts

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance, interest_rate):
        # calling the parent init to initialize account_holder and initial_balance
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate #unique child attribute

    # Method to add interested to the balance
    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)# deposit is not overriden so we can call with self to get the functionality
        # from the parent class
        print(f"Interest {interest} added to the balance")

    # withdraw from savings
    # overriding the parent withdraw
    # SavingsAccount.withdraw()
    def withdraw(self, amount):
        if amount > 500:
            print("Withdrawal limit exceeded")
        else:
            # using the super to call the parent withdraw method
            # BankAccount.withdraw()
           super().withdraw(amount)
  
        #withdraw was overridden so we use super to apply the functionality from the parent class

# checking account
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, initial_balance, transaction_fee):
        super().__init__(account_holder, initial_balance)
        self.transaction_fee = transaction_fee

    # overriding the parent withdraw method to include the transaction fee
    def withdraw(self, amount):
        total_amount = amount + self.transaction_fee
        if total_amount <= self.get_balance():
            self.set_balance(self.get_balance() - total_amount)
            print(f"Withdrawn: {amount}, Transaction Fee: {self.transaction_fee}")
        else:
            print(f"Insufficient balance for withdrawal and transaction fee")

savings = SavingsAccount("Ryan", 1500, 0.01)
checking = CheckingAccount("Ryan", 1500, 30)
# Savings Account Usage
savings.add_interest() #adds interest to the balance
savings.withdraw(499)
print(savings.get_balance())

# Checking Account Usage
checking.deposit(500)
checking.withdraw(300)
print(f"Checking Account Balance: {checking.get_balance()}")

# updating account holders from the parent methods
savings.set_account_holder("Ruben")
checking.set_account_holder("Selena")
