class Multibases(type):
    def __new__(cls,clsname,bases,attrs):
        if len(bases)>1:
            raise TypeError("Jest możliwe tylko jednodziedziczenie!")
        return super().__new__(cls,clsname,bases,attrs)

class Base(metaclass=Multibases):
    pass


class A(Base):
    pass

class B(Base):
    pass

class C(A,B):
    pass


class Info:
    pass

class Next(A,Info):
    pass


class AXX:
    pass

class Last(AXX,Info):
    pass
