print("####### Bank Accounts  #############")
import random

class BankAccount:
    def __init__(self, bank_name, owner_name):
        import random
        self.balance = 0
        self.bank_name = bank_name
        self.account_number = random.randint(10000000, 99999999)
        self.owner_name = owner_name
        pass

    def deposit(self, amount) -> None :
        self.balance = self.balance + amount
        print(f"Deposit of {amount} accepted. New balance is {self.balance} ")

    def withdraw(self, amount) -> float:
        if amount > self.balance:
            no = "Sorry you don't have that much in your bank account!"
            # raise ValueError(no) <- Might want to do this.
            print(no) #<- this is probably fine though. 
            return(0)
        else:
          self.balance = self.balance - amount
          print(f"Withdraw of {amount} approved. Returning to client")
          # if we withdraw, $$ should go straight from balance, through register, and back
          # to transaction maker. Thus this should _return_ that withdraw. 
          return(amount) 
    
    def __str__(self):
        rt = (f"Bank Name: {self.bank_name} "\
              f"Account Holder: {self.owner_name} "\
              f"Account Number: {str(self.account_number)} " \
              f"Balance: {str(self.balance)}")
        return(rt)
    

citi = BankAccount(bank_name="Citi", owner_name="Tony Fraser")
citi.deposit(amount=1000)
citi.withdraw(amount=1)
print(citi)

nfcu = BankAccount(bank_name="Navel Federal Credit Union", owner_name="Tony Fraser")
nfcu.deposit(amount=1001)
nfcu.withdraw(amount=1002)
print(nfcu)
print("####################################")

# ####### Bank Accounts  #############
# Deposit of 1000 accepted. New balance is 1000 
# Withdraw of 1 approved. Returning to client
# Bank Name: Citi Account Holder: Tony Fraser Account Number: 44353180 Balance: 999
# Deposit of 1001 accepted. New balance is 1001 
# Sorry you don't have that much in your bank account!
# Bank Name: Navel Federal Credit Union Account Holder: Tony Fraser Account Number: 48245026 Balance: 1001
# ####################################


print("#########  Boxes  ##################")

import math

class Box:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def render(self):
        """ prints to the screen a box made with asterisks of length times width """
        for _ in range(self.width):
            print('*' * self.length)

    def invert(self):
        """ switches length and width with each other """
        self.length, self.width = self.width, self.length

    def get_area(self):
        """ returns area """
        return self.length * self.width

    def get_perimeter(self):
        """ returns perimeter """
        return 2 * (self.length + self.width)

    def double(self):
        """ doubles the sides """
        self.length *= 2
        self.width *= 2

    def __eq__(self, other):
        """ sees if other box is same size """
        return self.length == other.length and self.width == other.width

    def get_dim(self):
        return (self.length, self.width)

    def combine(self, other):
        self.length += other.length
        self.width += other.width

    def get_hypot(self):
        return math.sqrt(self.length**2 + self.width**2)
    
    def __str__(self): 
        return f"Length: {self.length}, Width: {self.width}"
    def print_dim(self):
        """ prints to screen the length and width details of the box """
        print(self.__str__())

#1
box1 = Box(5, 10)
box2 = Box(3, 4)
box3 = Box(5, 10)

#2
box1.print_dim()
box2.print_dim()
box3.print_dim()

##3
print(box1 == box2)  # False
print(box1 == box3)  # True

#4
box1.combine(box3)

#5
box2.double()

#6
box1.combine(box2)
box1.print_dim()
box2.print_dim()
print("####################################")

# #########  Boxes  ##################
# Length: 5, Width: 10
# Length: 3, Width: 4
# Length: 5, Width: 10
# False
# True
# Length: 16, Width: 28
# Length: 6, Width: 8
# ####################################