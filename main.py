from CurrentAccount import CurrentAccount
from SavingsAccount import SavingsAccount

ca1=CurrentAccount(100000)
ca1.deposit()
ca1.display_balance()

ca1.withdraw(5000)
ca1.calculate_interest()

#output
# Deposit amount:  100000
# balance amount :  100000
# withdrawal amount is : 5000 
#  current balance is:  95000




sa1=SavingsAccount(200000)
sa1.deposit()
sa1.display_balance()
sa1.withdraw(5000)
sa1.calculate_interest()


#output
# Deposit amount:  200000
# balance amount :  200000
# withdrawal amount is : 5000 
#  current balance is:  195000
# interest amount:  9750.0

print("stop")