class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 1000
        
    def get_balance(self):
        return f'Your total balance is {self.balance}'
    
    def withdraw(self, amount):
        if self.min_withdraw < 100:
            return f'Minimum withdraw range is {self.min_withdraw}'
        elif self.max_withdraw > 10000:
            return f'Maximum withdraw range is {self.max_withdraw}'
        elif amount > self.balance:
            return f'Your amount is greater than your balance'
        else:
            self.balance = self.balance - amount

            return f'You successfully withdraw {amount}'
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        return f'Successfully deposit {amount}' 
        
        
my_balance = Bank(8000)
print(my_balance.withdraw(5000))
print(my_balance.get_balance())
print(my_balance.deposit(1500))
print(my_balance.get_balance())

        
        