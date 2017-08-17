class Fraction:
    '''This class treats numbers as fractions and does fraction arithematis'''
    # the parameters
    num = 1
    den = 1
    # First the constructor that assigns the values to num and den
    def __init__(self, up, down):
        try:
            if not isinstance( up, int ) or not isinstance( up, int ):
                up = int(up)
                down = int(down)
                print("NOTE: the numerator and denominator of a fraction both must be integer!")
                raise TypeError
        except:
            g = gcd(up,down)
            self.num = up // g
            self.den = down // g
    # need a method to print it as num/den- we write an overirde of __str__ method
    def __str__(self): #note no declaration of override needed
        return str(self.num) + "/" + str(self.den) #note - you must cast to string
    # Override the __add__(a,b) method to use a+b as addition between two fractions

    # A helper function to simplify fractions - declare it static method
    @staticmethod
    def gcd(a, b):
        if a > b: a, b = b, a
        while True:
            if b % a == 0: return a
            a, b = b % a, a

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    # Override the __sub__(a,b) method to use a-b of two fractions
    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    #Override __mul__(a,b) method for x operator
    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    # __truediv__

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden)

#lets use the class
if __name__ == "__main__": ## the main method
#
    myFrac = Fraction(3,5) # no new command needed to create the object
    # now we print the fraction
    print(myFrac)
#     # adding two fractions
    f1 = Fraction(3,5)
    f2 = Fraction(2,3)
    f3 = f1 + f2
    print(str(f1) + "+" + str(f2) + "=" + str(f3))
#     # subtracting
    f1 = Fraction(1,2)
    f2 = Fraction(1,8)
    f3 = f1 - f2
    print(str(f1) + "-" + str(f2) + "=" + str(f3))
    # note common factors - need gcd to simplify
    # print(gcd(12,8))
    # now we use gcd() to simplify the results
    f1 = Fraction(3,4)
    f2 = Fraction(2,7)
    f3 = f1 - f2
    # g = gcd(f3.num, f3.den)
    # f3.num = f3.num//g
    # f3.den = f3.den//g
    print(str(f1) + "-" + str(f2) + "=" + str(f3))
    f4 = f1 * f2
    print(str(f1) + "x" + str(f2) + "=" + str(f4))
    f5 = f1 / f2
    print(str(f1) + " divBy " + str(f2) + "=" + str(f5))
    # check exception raising and correcting to int types
    f6 = Fraction(1, 3)
    print(f6)
