from collections import deque
from grafos.grafo import Grafo

#class Grafo:
#    arestas = {}
#    vertices = []
#    pesos = {}
#    rotulos = {}

def find(self, parent, i): 
        if parent[i] == i: 
            return i    #so retorna se o metodo achar o pai da FLORESTA LOCAL
        return self.find(parent, parent[i]) 

def union(self, parent, rank, ancestralDeU, ancestralDeV):

    # quem tiver o menor rank, recebe o de maior rank como pai  
    if rank[ancestralDeU] < rank[ancestralDeV]: 
        parent[ancestralDeU] = ancestralDeV 
    elif rank[ancestralDeU] > rank[ancestralDeV]: 
        parent[ancestralDeV] = ancestralDeU 

    #se os ranks forem iguais, o ancestral final de v vira o ancestral final de u
    else : 
        parent[ancestralDeV] = ancestralDeU 
        rank[ancestralDeU] += 1
def Kruskal(g): 
    
    resultado = []
    set_arestas = {tuple(sorted([u, v])) for u, vs in g.arestas.items() for v in vs}
    arestas_ordenada = sorted(set_arestas, key=lambda e: self.pesos[e])

    pai = [] ; rank = []
    i = 0 #index pra percorrer cada possivel aresta na entrada
    e = 0 #numero de arestas em resultado[] (arestas da saida)
    
    for node in range(len(g.vertices)): 
        pai.append(node) 
        rank.append(0) 
  
    while e < len(g.vertices) -1 : #enquanto a arvore nao estiver completa...

        ancestralDeU = self.find(pai, arestas_ordenada[i][0]) #u
        ancestralDeV = self.find(pai ,arestas_ordenada[i][1]) #v

        if ancestralDeU != ancestralDeV: 
            e = e + 1     
            resultado.append(([arestas_ordenada[i][0],arestas_ordenada[i][1]])) 
            self.union(pai, rank, ancestralDeU, ancestralDeV)             
        i = i + 1 # arestas_ordenadas[(i=0),(i=1), ... ,(i=vertices -1 )]

    print ("Peso da arvore:")
    pesoTotal = 0
    for aresta in resultado:
        pesoTotal = pesoTotal + g.pesos["aresta"]
    print ("%d" % (peso))
    
    print ("Arestas na arvore:")
    for aresta  in resultado: 
        print ("%d -- %d" % (aresta[0],aresta[1])) 
