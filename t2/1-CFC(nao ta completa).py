#  1-CFC
from grafo import Grafo

def DFS_Visit(g, v, visitado, tempoVisita, antecessor, tempoFinal, tempo):
    visitado[v] = True
    tempo = tempo + 1
    tempoVisita[v] = tempo
    
    for u in g.vizinhos(v): # vizinhosSaintes (arrumar)
        if visitado[u] == False:
            antecessor[u] = v
            DFS_Visit(g, u, visitado, tempoVisita, antecessor, tempoFinal, tempo)
    
    
    tempo = tempo + 1
    tempoFinal[v] = tempo
#

def DFS(g, visitado, tempoVisita, antecessor, tempoFinal):
    # configurando todos os vértices 
    
    visitado = {x:False for x in g.vertices} # Cv←false ∀v ∈ V
    tempoVisita = {x:float('inf') for x in g.vertices} # Tv ←∞ ∀v ∈ V
    tempoFinal = {x:float('inf') for x in g.vertices} # Fv ←∞ ∀v ∈ V
    antecessor = {x:None for x in g.vertices} # Av ←∞ ∀v ∈ V
    
    tempo = 0
    
    for u in g.vertices:
        if visitado[u] == False:
            DFS_Visit(g, u, visitado, tempoVisita, antecessor, tempoFinal, tempo)
#

# algoritmo auxiliar DFS-Alterado
def DFS_Alterado(gTransposto, visitado, tempoVisita, antecessor, tempoFinal):
    visitado = {x:False for x in g.vertices} # Cv←false ∀v ∈ V
    tempoVisita = {x:float('inf') for x in g.vertices} # Tv ←∞ ∀v ∈ V
    tempoFinal = {x:float('inf') for x in g.vertices} # Fv ←∞ ∀v ∈ V
    antecessor = {x:None for x in g.vertices} # Av ←∞ ∀v ∈ V
    
    tempo = 0
    
    # pega em ordem decrescente de F
    teste = True
    while (teste):
        teste = False
        maior = -1
        maior_indice = -1
        for i in g.vertices:
            if tempoFinal[i] > maior and visitado[i] == False:
                teste = True
                maior = tempoFinal[i]
                maior_indice = i
        
        if maior_indice != -1:
            DFS_Visit(gTransposto, maior_indice, antecessor, visitado, tempoVisita, tempoFinal, tempo)
            
#
g = Grafo(True, False)

# Vetor C/Visitado
# Vetor T/tempo de visita
# Vetor A'/Antecessor 
# Vetor F/ tempo que é finalizado
    
vertices = g.vertices
visitado = {}
tempoVisita = {}
antecessor = {}
tempoFinal = {}
print("HelloWood2")
DFS(g, visitado, tempoVisita, antecessor, tempoFinal)
print("HelloWood9?")
gTransposto = g.transposta()
print("HelloWood1")
DFS_Alterado(gTransposto, visitado, tempoVisita, antecessor, tempoFinal)

print("HelloWood")
# Saida

for i in g.vertices:
    if (antecessor[i] == None):
        saida = str(i) + (", ")
    else:
        saida = str(i) + (": ")

print(saida)
