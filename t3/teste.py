from itertools import chain, combinations
from grafo import Grafo
g = Grafo(False,False)


def potencia(c):
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]
def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

#print(potencia([1,2,3,4]))
a = [1,2,3]
b = powerset(a)
print(a)
print(list(b))
#print(powerset([1,2,3]))

