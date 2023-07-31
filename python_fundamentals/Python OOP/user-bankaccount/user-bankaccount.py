from BankAccount import BankAccount
class User:
    def init(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self,amount):
        self.account.deposit(amount)

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        print('--------------------------')
        print ("User Informations ")
        print('--------------------------')
        print(f'Name : {self.name}')
        print('--------------------------')
        print(f'E-mail : {self.email}')
        print('--------------------------')
        self.account.display_account_info()


u1 = User('saif','saif@gmail.com')
u1.make_deposit(20)
u1.display_user_balance()
class BankAccount:
    def init(self, int_rate = 0.01, balance = 0):
        self.int_rate =  int_rate
        self.balance = balance

    def deposit(self,amount):
        self.balance+=amount
        print('--------------------------')
        print('Deposit Done Successfully')
        print('--------------------------')
        print(f'Your New Balance : {self.balance}')
        print('--------------------------')

    def withdraw(self,amount):
        if(self.balance < amount):
            self.balance-=5
            print('--------------------------')
            print('Insufficient funds: Charging a $5 fee')
            print('--------------------------')
            print(f'Your New Balance : {self.balance}')
            print('--------------------------')
        else:
            self.balance-=amount
            print('--------------------------')
            print('Withdraw Done Successfully')
            print('--------------------------')
            print(f'Your New Balance : {self.balance}')
            print('--------------------------')

    def display_account_info(self):
        print('--------------------------')
        print('Account Informations ')
        print('--------------------------')
        print(f'Your Balance is : {self.balance}')
        print('--------------------------')
        print(f'Your interest rate is : {self.int_rate}')
        print('--------------------------')
def yield_interest(self):
        if(self.balance>0):
            self.balance += self.balance*self.int_rate
            print('--------------------------')
            print('Yield Interest Done Successfully')
            print(f'Your New Balance : {self.balance}')
            print('--------------------------')
        else:
            print('--------------------------')
            print('You have 0$,Process Denied')
            print('--------------------------')

acc1 = BankAccount(0.01,50)
acc1.deposit(10)
acc1.withdraw(60)
acc1.display_account_info()
acc1.yield_interest()