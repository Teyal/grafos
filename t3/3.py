from itertools import chain, combinations
from collections import defaultdict
import copy
from grafo import Grafo

def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def I(G):
    pass

def coloracao():
    g = Grafo(False,False)

    numSets = g.qtdVertices()
    X = [0]*(2**numSets)
    X[0]=0
    S = list(powerset(g.vertices))
    for s in S[1:]: # primeiro valor é ignorado pois é "()"
        _s = S.index(s)
        X[_s] = float('inf')
        _g = copy.deepcopy(g)
        _g.vertices = list(s)
        _g.arestas  = {u:v for u in list(s) for v in list(s) if v in g.arestas[u]}
        for I in I(_g):
            i = S.index(tuple(set(s)-set(I)))
            if X[i]+1 < X[_s]:
                X[_s] = X[i]+1 
        return X[-1]



