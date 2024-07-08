

class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email_args, password_args):
        self.email = email_args # this will create a variable even if we don't define them in line no 4 and 5 then also its okay
        self.password = password_args

    def login_confirm(self):
        if self.password == "pass123":
            print("allowed to enter")
        else:
            print("Not allowed")
#This is the end of the class

amit = VWOLoginPage("amit@gmail.com", "123")
amit.login_confirm()

shraddha = VWOLoginPage("ss#gmail.com", "pass123")
shraddha.login_confirm()