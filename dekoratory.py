import time

#przykład 1
def pomiarczasu(funkcja):
    def wrapper():
        wynik = []
        starttime = time.perf_counter()
        starttime = time.time()
        print(f'czas startu pomiaru: {starttime} s')
        funkcja()
        endtime = time.perf_counter()
        print(f'czas zakończenia pomiaru: {endtime} s')
        wynik.append(endtime-starttime)
        print(wynik)
    return wrapper



@pomiarczasu
def big_nb():
    sum([i**2 for i in range(10_000_000)])

big_nb()
