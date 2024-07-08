class VWOLogin:

    def __init__(self,email,password,name):
        self.__email = email
        self.__password = password
        self.name = name
    def login_confirm(self):
        if self.__email == "abc@gmail.com" and self.__password =="123":
            print("allowed")
        else:
            print("Not allowed")

page1 = VWOLogin("abc@gmail.com", "123", "pramod")
page1.login_confirm()
print(page1.name)

