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
