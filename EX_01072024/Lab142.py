class GF:

    def car(self):
        return "old car"


class F(GF):

    def car(self):
        return "Honda civic"


class S(F):

    # def car(self):
    #     return "Lambo"
    pass

son = S()
gf = GF()
print(gf.car())
print(son.car())
