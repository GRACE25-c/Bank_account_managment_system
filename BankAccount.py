from abc import ABC,abstractmethod

# creating a class an abstract class.
# we cannot create an object of an abstract class.

class BankAccount(ABC):

#constractor of the class
    def __init__(self,i_deposit):
        # self.i_withdrow=i_withdrow
        self.i_deposit=i_deposit
        #a private variable - encapsulation

        self.__Account_Balance=0
    
#create an abstract methord  
# THIS METHOD MUST BE INHERITED BY THE CHILED CLASS    
    @abstractmethod
    def calculate_interest(self):
        pass
    def display_balance(self):
        self.Account_Balance=self.__Account_Balance+self.i_deposit
        print("balance amount : ",self.Account_Balance)
        
    def Account_balance(self):
        return self.__Account_Balance
    def deposit(self):
    
        # self.deposit=deposit
        if type(self.i_deposit)=="str":
            return ValueError("diposit value is not an integer")
        elif self.i_deposit>0:
           print("Deposit amount: ",self.__Account_Balance+self.i_deposit)
           
        else:
            # self.Account_balance =self.Account_balance+self.deposit
            return ValueError ("deposit a positive amount")
    # def display_balance(self):
    #     print("balance amount : ",self.Account_balance)
        # print("Deposit amount: ",self.Account_balance+self.deposit)
        
    def withdraw(self,i_withdrow):
        self.i_withdrow=i_withdrow
        self.Account_balance=self.Account_Balance-self.i_withdrow
        if type(self.i_withdrow)=="str":
            return ValueError("diposit value is not an integer")
        elif self.i_withdrow<=self.Account_Balance:
            print("withdrawal amount is :",self.i_withdrow,"\n","current balance is: ",self.Account_balance)

        else:
            return ValueError ("the balance amount is smaller than your withdrawal amount")
    

  




