class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, name, initial_amount) -> None:
        self.name = name
        self.balance = initial_amount
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
        
    def get_balance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
        
    def deposite(self, amount):
        self.balance += amount
        print("\nDeposite completed.")
        self.get_balance()
        
    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry,Account '{self.name}' has only amount of ${self.balance}")
    
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("\nWithdraw completed.")
            self.get_balance()
            
        except BalanceException as error:
            print(f"\Withdraw interrupted.. {error}")
            
    def tranfermoney(self,amount, other):
        try:
            print("\n*************\n\nBeginning Tranfer.... 🚀")
            self.viable_transaction(amount)
            self.withdraw(amount)
            other.deposite(amount)
            print("\nTransfer completed...✅\n\n**************")
            
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")
            

class InterestRewardAccount(BankAccount):
    def deposite(self, amount):
        self.balance += amount * 1.05
        print("\nDeposite completed..")
        self.get_balance()
        

class SavingAccount(InterestRewardAccount):
    def __init__(self, name, initial_amount) -> None:
        super().__init__(name, initial_amount)
        self.fee = 5
        
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance -= amount + self.fee
            print("\nWithdraw completed..")
            self.get_balance()
            
        except BalanceException as error:
            print(f"\nWithdraw interrupted. ❌ {error}")
            
        
        
    