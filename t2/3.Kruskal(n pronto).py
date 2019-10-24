# -*- coding: utf-8 -*-
from collections import deque
from grafo import Grafo

#class Grafo:
#    arestas = {}
#    vertices = []
#    pesos = {}
#    rotulos = {}

def find(pai, i): 
        if pai[i] == i: 
            return i    #so retorna se o metodo achar o pai da FLORESTA LOCAL
        return find(pai, pai[i]) 

def union(pai, ancestralDeU, ancestralDeV):
    pai[ancestralDeV] = ancestralDeU 

def Kruskal(g): 
    
    resultado = []

    set_arestas = {tuple(sorted([u, v])) for u, vs in g.arestas.items() for v in vs}
    arestas_ordenada = sorted(set_arestas, key=lambda e: g.pesos[e])

    pai = [] 
    i = 0 #index pra percorrer cada possivel aresta na entrada
    e = 0 #numero de arestas em resultado[] (arestas da saida)
    
    for node in g.vertices: 
        pai.append(node) 
    while e < len(g.vertices) -1 : #enquanto a arvore nao estiver completa...

        ancestralDeU = find(pai, arestas_ordenada[i][0]) #u
        ancestralDeV = find(pai, arestas_ordenada[i][1]) #v

        if ancestralDeU != ancestralDeV: 
            e = e + 1     
            resultado.append(([arestas_ordenada[i][0],arestas_ordenada[i][1]])) 
            union(pai, ancestralDeU, ancestralDeV)             
        i = i + 1 # arestas_ordenadas[(i=0),(i=1), ... ,(i=vertices -1 )]

    print ("Peso da arvore:")
    pesoTotal = 0
    for aresta in resultado:
        pesoTotal = pesoTotal + g.pesos[tuple(aresta)]
    print ("%d" % (pesoTotal))
    
    print ("Arestas na arvore:")
    for aresta  in resultado: 
        print ("%d -- %d" % (aresta[0],aresta[1])) 


g = Grafo(False, True)
Kruskal(g)