class BankAccount(object):
    balance = 0
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "%s's account. Balance: $%.2f" % (self.name, self.balance)
    def show_balance(self):
        print ("Balance: $%.2f" % (self.balance))
    def deposit(self, amount):
        self.amount = amount
        if self.amount <= 0:
            print ("Wrong amount.")
        else:
            print ("Deposting: $%.2f" % (self.amount))
            self.balance += self.amount
            self.show_balance()
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print ("You ain't got that kind of dough!")
            return
        else:
            print (("Withdrawing: $%.2f:") % (self.amount))
            self.balance -= self.amount
            self.show_balance()
            
my_account = BankAccount("Julio")
print (my_account)
my_account.show_balance()
my_account.deposit(5000000)
my_account.withdraw(300)
print (my_account)