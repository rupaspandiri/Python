
class bankaccount:
    def _init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.amount=self.amount+amount
    def withdraw(self,amount):
        self.amount=self.amount-amount
        class display():
            print(self.name,"balance is",self.balance)
ba=bankaccount()
ba.depsit(1000)
ba.withdraw(500)
ba.display()
