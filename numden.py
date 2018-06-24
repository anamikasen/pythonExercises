class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def getNum(self):

        return self.num

    def getDen(self):

        return self.den

if __name__ == "__main__":
    myFraction = Fraction(3,5)
    print(myFraction.getNum())
    print(myFraction.getDen())
