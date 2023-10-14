#przykład 1
def witaj(imie):
    return f'dziękujemy za założenie konta {imie}'

def egzamin(imie,punkty,zaliczono):
    return f'osoba egzaminowana: {imie}, liczba punktów: {punkty}, zaliczenie: {zaliczono}'

def fx(a,b,c):
    return (a+b)*c

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(egzamin,"Olga",67,True))
print(osoba(fx,4,7,2))

#przykład 2
liczba = [4,5,24,12,778,-5,0,-12,455,67,99,100,3,8,-23,22]

parzyste = list(filter(lambda x:x%2==0,liczba))

print(parzyste)

cube = list(map(lambda a:a**3,liczba))
print(cube)

#przykład 3

def rejestracja(oplata):
    def lista_zawodnikow(nrlisty):
        return f'jesteś na liście zawodników nr {nrlisty}'

    def brak():
        return "brak wpłaty, uzupełnij w ciągu 3 dni!"

    def error():
        return "błąd systemu rozliczeniowego... powótrz wpłatę"

    if oplata == 1:
        return lista_zawodnikow
    elif oplata == 0:
        return brak
    else:
        return error

print(rejestracja(1)(356))
print(rejestracja(0)())
print(rejestracja(23423)())
