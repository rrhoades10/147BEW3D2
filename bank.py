class BankAccount: #parent class or super class
    def __init__(self, account_holder, initial_balance = 0):
        self.__balance = initial_balance
        self.account_holder = account_holder

    # getter for balance - Private
    def get_balance(self):
        return self.__balance
    
    # setter for balance - Private
    def set_balance(self, new_balance):
        self.__balance = new_balance

    # we dont technically need getters and setters for public attributes
    # but it is a nice way to format our code and make making changes/accessing those attributes
    # a little smoother
    # getter for account_holder
    def get_account_holder(self):
        return self.account_holder

    # setter for account_holder
    def set_account_holder(self, new_holder):
        self.account_holder = new_holder

    # Deposit Method
    def deposit(self, amount):
        if amount > 0:
            # this sets the balance to the current balance plus the amount we're depositing
            self.set_balance(self.get_balance() + amount)
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    # withdraw method
    def withdraw(self, amount):
        # if the amount we are withdrawing is greater than 0 and less than our current balance
        if 0 < amount < self.get_balance():
            # set the balance to the current balance - the amount to be withdrawn
            self.set_balance(self.get_balance() - amount)
            print(f"Withdrawn: {amount}")

my_account = BankAccount("Ryan")
print(f"Account Holder: {my_account.get_account_holder()}" )
print(f"Initial Balance: {my_account.get_balance()}")

my_account.deposit(1500)
print(f"Current Balance {my_account.get_balance()}")

# depositing a number < 0
my_account.deposit(-1)
# withdrawing 
my_account.withdraw(500)

my_account.set_account_holder("Selena")
print(my_account.get_account_holder())