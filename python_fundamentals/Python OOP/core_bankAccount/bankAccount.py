class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.init_rate= interes_rate
        self.balance = banlance
       
    def deposit(self, amount):
        self.balance +=amount
        return  self
       
    def withdraw(self, amount):
     if self.balance>= amount:
        self.balance-= amount
     else :
        print("insufison sold")
     return  self
       
    def display_account_info(self):
        print(f"balance :{ self.balance}")
      
    def yield_interest(self):
        itit_rate = self.init_rate * self.balance
        self.balance += self.init_rate
   
    @classmethod
    def print_all_accounts_info(cls):
        for account in cls.accounts:
            print(f"Interest Rate: {account.interest_rate}, Balance: {account.balance}")
            account1 = BankAccount(0.05, 1000)
            account2 = BankAccount(0.1, 500)