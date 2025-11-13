class BankAccount:
    def __init__(self,balance = 0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited :{amount}")
        else:
            print("Deposited amount must be positive")

    def withdrawl (self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawl :{amount}")
        else:
            print("Invalid Amount")
    
    def get_balance(self):
        print(f"Current Balance: ₹{self.__balance}")


account = BankAccount(1000)
account.deposit(500)
account.withdrawl(600)
account.get_balance()


