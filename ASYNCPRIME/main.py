import time
import concurrent.futures
from funkcja_prime import znajdz_sume_liczb_pierwszych

numbers = [(1,10_000),(3,50_000),(5_000,100_000),(4,900),(8_000,15_000),(95_000,133_000)]

def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.perf_counter()
        funkcja()
        endtime = time.perf_counter()
        wynik= endtime-starttime
        print(wynik)
    return wrapper

def run_heavy_function(params):
    return znajdz_sume_liczb_pierwszych(*params)

@pomiarczasu
def synchronicznie():
    for pairs in numbers:
        prime_suma = znajdz_sume_liczb_pierwszych(*pairs)
        print(prime_suma)
    print("czas wykonania zadania synchronicznie [s]:")


@pomiarczasu
def asynchronicznie():
    with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
        wynik = executor.map(run_heavy_function,numbers)
    print(list(wynik))
    print("czas wykonania zadania asynchronicznie [s]:")


def main():
    synchronicznie()
    print("_"*40)
    asynchronicznie()

if __name__ == '__main__':
    main()
