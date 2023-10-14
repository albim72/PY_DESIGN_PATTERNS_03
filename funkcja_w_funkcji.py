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
