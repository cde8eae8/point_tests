from random import *

def gen(name, arr):
    file = open(name, 'w')
    print(len(arr), file=file)
    for i in arr:
        print(i[0], i[1], file=file)
    file.close()

def f(n):
    return str(n) + '.test'

def randpoints(n = 100, min=-100000, max=100000):
    return [(randint(min, max), randint(min, max)) for i in range(n)]

gen(f(1), [(0, 0), (0, 0)])
gen(f(2), [(1, 1), (-1, -1)])
gen(f(3), [(-1, -1), (0, 0)])
gen(f(4), [(1, -1), (1, 0)])
for i in range(100):
    gen(f(1000 + i), randpoints())


