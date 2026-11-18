from BankAccount import BankAccount
#INHERITANCE : We inherits methords and propertice of perent class
class CurrentAccount(BankAccount):
    # def __init__(self,Account_Balance,deposit):
    #     super().__init__(self,Account_Balance,deposit)
    def dummymethod(self):
        print("this is a dummy method")
    def calculate_interest(self):
        interest=0
        return interest