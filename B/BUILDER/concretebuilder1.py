from builder import Builder
from prod1 import Product1

class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        self.reset()
        
    def reset(self):
        self._produkt = Product1()

    @property
    def product(self)->Product1:
        product = self._produkt
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._produkt.add("PartA1")

    def produce_part_b(self) -> None:
        self._produkt.add("PartB1")

    def produce_part_c(self) -> None:
        self._produkt.add("PartC1")
        
    
