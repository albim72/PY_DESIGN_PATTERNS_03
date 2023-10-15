odp = input("Czy Ziemia jest płaska? Chcesz nac odpowiedź? (t/n) ")

if odp.lower() == "t":
    required = True
else:
    required = False

def odpowiedz_old(self):
    return "Tak! Ziemia jest płaska!"

def error(self):
    return "brak odpowiedzi..."

#metaklasa opsująca przyszłych filozofów i naukowców
class SednoOdpowiedzi(type):
    def __init__(cls,clsname,bases,attrs):
        if required:
            cls.odpowiedz = odpowiedz_old
        else:
            cls.odpowiedz = error

class Arytoteles(metaclass=SednoOdpowiedzi):
    pass

class Platon(metaclass=SednoOdpowiedzi):
    pass

class SwTomasz(metaclass=SednoOdpowiedzi):
    pass

fil1 = Arytoteles()
print(f'Filozof {fil1.__class__.__name__} twierdzi: {fil1.odpowiedz()}')

fil2 = Platon()
print(f'Filozof {fil2.__class__.__name__} twierdzi: {fil2.odpowiedz()}')

fil3 = SwTomasz()
print(f'Filozof {fil3.__class__.__name__} twierdzi: {fil3.odpowiedz()}')
