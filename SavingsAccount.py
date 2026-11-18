# refering class define on in another nodeule/file
from BankAccount import BankAccount
class SavingsAccount(BankAccount):
    def dummy(self):
        pass
    def calculate_interest(self):
        intrest_amount=self.Account_balance*(5/100)
        # return intrest_amount
        print("interest amount: ",intrest_amount)
        return intrest_amount