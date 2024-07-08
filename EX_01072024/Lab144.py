class Father:

    def home(self):
        print("1BHK")

class Son(Father):

    def home(self):
        super().home() #Now son can call father home as well so this will print 1BHK and #BHK both, super can only give father and not grandfather
        print("3BHK")

    # pass

pramod = Son()
pramod.home()