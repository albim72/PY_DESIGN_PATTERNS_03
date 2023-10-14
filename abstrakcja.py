from abc import ABC,abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x=x

    def msg(self,m):
        return f'kod numer {m}'

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_x(self):
        return self.x*7


class Regular(Prototyp):

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def policz(self):
        return 2003

    def policz_x(self):
        return super().policz_x() + self.y*3


rg = Regular(4,7)
print(f'funkcja policz() -> {rg.policz()}')
print(f'funkcja policz_x() -> {rg.policz_x()}')

class Druga(Regular):
    pass

dr = Druga(5,9)
print(f'funkcja policz() -> {dr.policz()}')
print(f'funkcja policz_x() -> {dr.policz_x()}')
print(f'wiadomość: {dr.msg(45)}')
