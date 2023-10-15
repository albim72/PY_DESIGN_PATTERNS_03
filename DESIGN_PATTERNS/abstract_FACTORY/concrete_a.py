from abstract_a import AbstractProductA

class ConreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "wynik: produkt A1!"
    
class ConcereteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "wynik: produkt A2!"
