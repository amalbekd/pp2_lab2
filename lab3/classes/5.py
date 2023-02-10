class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
        
    def deposit(self, dep):
        self.balance += dep
        print('Deposit Accepted')
        
    def withdraw(self, wd):
        if self.balance >= wd:
            self.balance -= wd
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')