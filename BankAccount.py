class BankAccount:

    balance = 0
    interest = .01
    accounts = []

    def __init__(self, intRate = interest, bal = balance):
        self.intRate = intRate
        self.balance = bal
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Insufficient funds: charging a $5 fee')
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self

    def displayAccountInfo(self):
        print(f'Account:  Balance: ${self.balance}')

    def yieldInterest(self):
        if self.balance > 0:
            sum = self.balance * self.intRate
            self.balance += sum
            return self
        else:
            return self

    @classmethod
    def bankAccountInfo(cls):
        for i in cls.accounts:
            print(i.balance, i.intRate)



acc1 = BankAccount()
acc2 = BankAccount()

acc1.deposit(100).deposit(100).deposit(100).withdraw(50).yieldInterest().displayAccountInfo()
acc2.deposit(100).deposit(100).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yieldInterest().displayAccountInfo()

BankAccount.bankAccountInfo()