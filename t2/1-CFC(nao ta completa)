from collections import deque
from grafo import Grafo

#  1-CFC

# Vetor C/Visitado
# Vetor T/tempo de visita
# Vetor A'/Antecessor 
# Vetor F/ tempo que é finalizado

visitado = []
tempoVisita = []
antecessor = []
tempoFinal = []

g = Grafo(True, False)

DFS(g, visitado, tempoVisita, antecessor, tempoFinal)

aTransposto = {}

for g.arestas in antecessor:
    aTransposto = aTransposto 


private DFS(g, visitado, tempoVisita, antecessor, tempoFinal):

    # configurando todos os vértices 
    
    visitado = {x:False for x in vertices} # Cv←false ∀v ∈ V
    tempoVisita = {x:float('inf') for x in vertices} # Tv ←∞ ∀v ∈ V
    tempoFinal = {x:float('inf') for x in vertices} # Fv ←∞ ∀v ∈ V
    antecessor = {x:None for x in vertices} # Av ←∞ ∀v ∈ V
    
    tempo = 0
    
    for u in g.vertices():
        if visitado[u] = False:
            DFS-Visit(g, u, visitado, tempoVisita, antecessor, tempoFinal, tempo)
    
    return(visitado, tempoVisita, antecessor, tempoFinal)


private DFS-Visit(g, v, visitado, tempoVisita, antecessor, tempoFinal, tempo):
    visitado[v] = True
    tempo = tempo + 1
    tempoVisita[v] = tempo
    
    for u in g.vizinhos(v):
        if visitado[u] = False:
            antecessor[u] = v
            DFS-Visit(g, u, visitado, tempoVisita, antecessor, tempoFinal, tempo):
            
    tempo = tempo + 1
    tempoFinal[v] = tempo
    

# Saida
