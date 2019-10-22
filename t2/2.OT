from collections import deque
from grafo import Grafo

#  2-OT

# Vetor C/Visitado
# Vetor T/tempo de visita
# Vetor F/ tempo que é finalizado

g = Grafo(True, False)

# configurando todos os vertices

visitado = {x:False for x in vertices} # Cv←false ∀v ∈ V
tempoVisita = {x:float('inf') for x in vertices} # Tv ←∞ ∀v ∈ V
tempoFinal = {x:float('inf') for x in vertices} # Fv ←∞ ∀v ∈ V

# configurando tempo de inicio

tempo = 0

# criando lista com os vertices topologicamente ordenados

O = []

for u in g.vertices():
    if visitado[u] = False:
        DFS_Visit_OT(g, u, visitado, tempoVisita, tempoFinal, tempo, O)
        
return O

private DFS_Visit_OT(g, v, visitado, tempoVisita, tempoFinal, tempo, O):
    visitado[v] = True
    tempo = tempo + 1
    tempoVisita = tempo
    
    for u in g.vizinhos(v):
        if visitado[u] = False:
            DFS_Visit(g, u, visitado, tempoVisita, tempoFinal, tempo)
    
    tempo = tempo + 1
    tempoFinal = tempo
    
    # adiciona o vertice v no inicio da lista O
    
    O = v + O
            
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
