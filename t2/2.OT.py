from grafo import Grafo

def DFS_Visit_OT(g, v, visitado, tempoVisita, tempoFinal, tempo, O):
    
    visitado[v] = True
    tempo = tempo + 1
    tempoVisita[v] = tempo
    
    if v in g.arestas.keys():
        for u in g.vizinhos(v):
            if visitado[u] == False:
                DFS_Visit_OT(g, u, visitado, tempoVisita, tempoFinal, tempo, O)
    
    tempo = tempo + 1
    tempoFinal = tempo
    
    # adiciona o vertice v no inicio da lista O
    
    O.insert(0, v)
#

# Vetor C/Visitado
# Vetor T/tempo de visita
# Vetor F/ tempo que é finalizado

g = Grafo(True, False)

# configurando todos os vertices

visitado = {x:False for x in g.vertices} # Cv←false ∀v ∈ V
tempoVisita = {x:float('inf') for x in g.vertices} # Tv ←∞ ∀v ∈ V
tempoFinal = {x:float('inf') for x in g.vertices} # Fv ←∞ ∀v ∈ V

# configurando tempo de inicio

tempo = 0

# criando lista com os vertices topologicamente ordenados

O = []

for u in g.vertices:
    if visitado[u] == False:
        DFS_Visit_OT(g, u, visitado, tempoVisita, tempoFinal, tempo, O)

print(O)
