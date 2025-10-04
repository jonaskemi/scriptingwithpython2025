# Task 1: Making the base class, BankAccount
class BankAccount:
    account_holder = ""
    balance = 0 
    
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        
    # reused in child classes
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")
        return self.balance

    # reused in child classes
    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive and less than or equal to the balance.")
        return self.balance

    # reused in child classes
    def account_info(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.balance:.2f} NOK"

# Task 1b: Making the first child class; SavingsAccount
class SavingsAccount(BankAccount):
    interest_rate = 0.02

    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        if interest_rate < 0:
            raise ValueError("interest_rate must be non-negative")
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return self.balance
    
# Task 1c: Making the second child class; CheckingAccount
class CheckingAccount(BankAccount):
    transaction_fee = 10 # 10 NOK fee per transaction
    
    # Withdraw method with fee reusing the base class withdraw method using super() 
    def withdraw(self, amount):
        if amount <= 0: # Check for negative or zero withdrawal
            raise ValueError("Withdrawal amount must be positive.")
        total_amount = amount + self.transaction_fee
        if total_amount > self.balance: # Check if balance is sufficient
            raise ValueError("Insufficient funds for this withdrawal including transaction fee.")
        return super().withdraw(total_amount) # Withdrawal from balance logic is used from base class
    
    
    def __init__(self, account_holder, balance=0, transaction_fee=10):
        super().__init__(account_holder, balance)
        self.transaction_fee = transaction_fee