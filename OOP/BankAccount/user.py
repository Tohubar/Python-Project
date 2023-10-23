from account import *

tohu = BankAccount("Tohubar", 1000)
arman = BankAccount("Arman", 2000)

# tohu.get_balance()
# arman.get_balance()

# tohu.deposite(100)
# arman.deposite(200)

# tohu.withdraw(2000)
# tohu.withdraw(200)

#tohu.tranfermoney(300, arman)

munni = InterestRewardAccount("Munni", 3000)
tinni = SavingAccount("Tinni", 2500)
        
munni.deposite(100)
tinni.deposite(200)

munni.withdraw(100)
tinni.withdraw(200)

munni.tranfermoney(3000, tinni)
    