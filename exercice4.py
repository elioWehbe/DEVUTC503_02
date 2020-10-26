from fractions import Fraction
def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n
class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, "/", self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)


    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden=self.den*otherfraction.den
        common=gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def simplifie(a,b):
     num=a
     den=b
     common=gcd(a,b)
     return Fraction(num//common,den//common)
f1=Fraction.simplifie(100,50)
print(f1)
f2=Fraction(22,7)
f3= Fraction(10,2)
f4 = f2+ f3
print(f4)
f5=Fraction(22,7)
f6= Fraction(10,2)
f7= f5*f6
print(f7)