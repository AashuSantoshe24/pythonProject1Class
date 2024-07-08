class BankAccount:

    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def __withdraw(self, amount):
        self.balance -= amount

    def __show_balance(self):
        print("your balance is", self.balance)

    def if_you_are_authenticated(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("Not allowed")

    def if_you_are_auth_uset(self, auth, amount):
        if auth:
            self.__withdraw(amount=amount)
        else:
            print("Not allowed")

jp_chase = BankAccount()
print(jp_chase.balance)
jp_chase.deposit(100)
jp_chase.if_you_are_authenticated(True)
jp_chase.if_you_are_auth_uset(True, 99)
jp_chase.if_you_are_authenticated(True)

secret_pass = input("Enter your PIN")
your_amount = int(input("Enter your amt to withdraw"))
if secret_pass == "1234":
     jp_chase.if_you_are_auth_uset(True, amount=your_amount)
     jp_chase.if_you_are_authenticated(True)
else:
    jp_chase.if_you_are_auth_uset(False)