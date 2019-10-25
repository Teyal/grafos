# -*- coding: utf-8 -*-
from grafo import Grafo
import copy

g = Grafo(True, False)

#  1-CFC

def reset():
    visitado = {x:False for x in g.vertices} # Cv←false ∀v ∈ V
    tempoVisita = {x:float('inf') for x in g.vertices} # Tv ←∞ ∀v ∈ V
    tempoFinal = {x:float('inf') for x in g.vertices} # Fv ←∞ ∀v ∈ V
    antecessor = {x:None for x in g.vertices} # Av ←∞ ∀v ∈ V
    return (visitado, tempoVisita, antecessor, tempoFinal)

def vizinhos(d, v):
        return d[v]

def DFS_Visit(g, v, visitado, tempoVisita, antecessor, tempoFinal, tempo):

    visitado[v] = True
    tempo = tempo + 1
    tempoVisita[v] = tempo
    if v in g.arestas.keys():
        for u in g.vizinhos(v): 
            if visitado[u] == False:
                antecessor[u] = v
                tempo = DFS_Visit(g, u, visitado, tempoVisita, antecessor, tempoFinal, tempo)
    
    
    tempo = tempo + 1
    tempoFinal[v] = tempo
    return tempo
#

def DFS(g, visitado, tempoVisita, antecessor, tempoFinal):
    # configurando todos os vértices
    tempo = 0
    
    for u in g.vertices:
        if visitado[u] == False:
            tempo = DFS_Visit(g, u, visitado, tempoVisita, antecessor, tempoFinal, tempo)
                
#    return(visitado, tempoVisita, antecessor, tempoFinal)
#

# algoritmo auxiliar DFS-Alterado
def DFS_Alterado(gTransposto, vertices, visitado, tempoVisita, antecessor, tempoFinal):
    
    tempo = 0
    
    for u in vertices:
        if visitado[u] == False:
            tempo = DFS_Visit(gTransposto, u, visitado, tempoVisita, antecessor, tempoFinal, tempo)

# Vetor C/Visitado
# Vetor T/tempo de visita
# Vetor A'/Antecessor 
# Vetor F/ tempo que é finalizado

visitado, tempoVisita, antecessor, tempoFinal = reset()
DFS(g, visitado, tempoVisita, antecessor, tempoFinal)
auxiliar = copy.deepcopy(g)
auxiliar.arestas = g.transposta()
#print(id(g))
#print(id(auxiliar))
#print(g.arestas)
#print(auxiliar.arestas)
#print(visitado)
print(g.vertices)
print(tempoVisita)
print(tempoFinal)
vertices_ordenados = sorted(g.vertices, key=lambda e: tempoFinal[e], reverse=True)
print(vertices_ordenados)
DFS_Alterado(auxiliar, vertices_ordenados, *reset())

# Saida
#saidaSafe = [[]]
