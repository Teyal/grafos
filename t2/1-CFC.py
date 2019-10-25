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

    #deveria ter uma maneira d fazer uma lista e retornar ela p poder ordenar mais rapido e poder imprimir o resultado final
    visitados = [v]

    visitado[v] = True
    tempo = tempo + 1
    tempoVisita[v] = tempo
    if v in g.arestas.keys():
        for u in g.vizinhos(v): 
            if visitado[u] == False:
                antecessor[u] = v
                tempo, visitados_aux = DFS_Visit(g, u, visitado, tempoVisita, antecessor, tempoFinal, tempo)
                visitados = visitados + visitados_aux
    
    tempo = tempo + 1
    tempoFinal[v] = tempo
    return (tempo, visitados)
#

def DFS(g, visitado, tempoVisita, antecessor, tempoFinal):
    # configurando todos os vértices
    tempo = 0
    
    ordem_visitados = []
    for u in g.vertices:
        if visitado[u] == False:
            tempo, visitados = DFS_Visit(g, u, visitado, tempoVisita, antecessor, tempoFinal, tempo)
            ordem_visitados = visitados + ordem_visitados
                
    return ordem_visitados
#    return(visitado, tempoVisita, antecessor, tempoFinal)
#

# algoritmo auxiliar DFS-Alterado
def DFS_Alterado(gTransposto, vertices, visitado, tempoVisita, antecessor, tempoFinal):
    
    tempo = 0
    cfc = []
    for u in vertices:
        if visitado[u] == False:
            tempo, visitados = DFS_Visit(gTransposto, u, visitado, tempoVisita, antecessor, tempoFinal, tempo)
            cfc.append(visitados)
    return cfc

# Vetor C/Visitado
# Vetor T/tempo de visita
# Vetor A'/Antecessor 
# Vetor F/ tempo que é finalizado

visitado, tempoVisita, antecessor, tempoFinal = reset()
vertices_ordenados = DFS(g, visitado, tempoVisita, antecessor, tempoFinal)
auxiliar = copy.deepcopy(g)
auxiliar.arestas = g.transposta()
resposta = DFS_Alterado(auxiliar, vertices_ordenados, *reset())
for i in resposta:
    print(", ".join(map(str, i)))
