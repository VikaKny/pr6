class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def deposite(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            return "Недостатньо коштів"

    def get_balance(self):
        return self.__balance

account1 = BankAccount("Іван", 150)
account2 = BankAccount("Микола", 300)
account3 = BankAccount("Юра", 50)

account1.deposite(100)
account1.withdraw(50)
print(account1._BankAccount__owner, account1.get_balance())

account2.deposite(1000)
account2.withdraw(20)
print(account2._BankAccount__owner, account2.get_balance())

account3.deposite(70)
account3.withdraw(200)
print(account3._BankAccount__owner, account3.get_balance())

