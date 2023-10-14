#przykład 1
def liczby():
    for i in range(17):
        yield i*2

print(liczby())
for p in liczby():
    print(p)

#przykład 2

def wznowienia(n,k):
    print("wstrzymanie działania...")
    yield 1001
    print("wznowienie działania!")

    print("wstrzymanie działania...")
    yield n+k
    print("wznowienie działania!")

    print("wstrzymanie działania...")
    yield n-k
    print("wznowienie działania!")

    print("wstrzymanie działania...")
    yield n*k
    print("wznowienie działania!")

    print("wstrzymanie działania...")
    yield n/k
    print("wznowienie działania!")

    print("wstrzymanie działania...")
    yield n**k
    print("wznowienie działania!")

print(wznowienia(4,5))

for i in wznowienia(12,8):
    print("_"*30)
    print(type(i))
    print(f'zwrócono wartość {i}')

#przykład 3
def complexgen():
    x=0
    while True:
        print("x - print1")
        y = yield x
        print("x - print2")
        if y is None:
            x = x+1
        else:
            x=y

g = complexgen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(g.send(123))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

