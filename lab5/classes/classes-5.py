class account:
    def __init__(self,owner, balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,add):
        self.add=self.balance+add 
        print("The balance is" ,self.owner,": ", self.add)
    def withdraw(self,minimum):
        self.minimum=minimum
        if minimum>self.balance:
            print("You do not have enough cash")
        else:
            self.balance=self.add-minimum
            print("The balance is",self.owner," :", self.balance)


x=account('Georgia',3900)
x.deposit(1100)
x.withdraw(4300)

y=account('John',7200)
y.deposit(8000)
y.withdraw(2000)
y.withdraw(1500)