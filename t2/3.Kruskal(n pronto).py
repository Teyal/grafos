#vou acabar hj

from collections import deque
from grafo import Grafo

def Kruskal(self): 

    resultado = [] 
    
    g = Grafo(false, true)

    i = 0 
    e = 0 

    g =  sorted(g,key=lambda item: item[2]) 

    pai = [] ; rank = [] 

    for node in range(self.V): 
        pai.append(node) 
        rank.append(0) 
  
    while e < self.V -1 : 

        u,v,p =  g[i] 
        i = i + 1
        x = self.find(pai, u) 
        y = self.find(pai ,v) 

        if x != y: 
            e = e + 1     
            resultado.append([u,v,p]) 
            self.union(pai, rank, x, y)             

    print ("Peso da arvore:")
    pesoTotal = 0
    for u,v,peso  in resultado:
        pesoTotal = pesoTotal + peso
    print ("%d" % (peso))
    
    print ("Arestas na arvore:")
    for u,v,peso  in resultado: 
        print ("%d -- %d" % (u,v)) 
