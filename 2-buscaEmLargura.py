from collections import deque
from grafo import Grafo

g = Grafo()

s = 2 # trocar por: s = g.vertice[n]
vertices = g.vertices

visitado = {x:False for x in vertices} # Cv←false ∀v ∈ V
d = {x:float('inf') for x in vertices} # Dv ←∞ ∀v ∈ V

# niveis = [[s]]

'''o resultado deve ser: [ [s]  [N(s)] [N(N(s))]]'''

# Configurando o vértice de origem

visitado[s] = True # Cs←true
d[s] = 0 # Dv <- 0

# preparando fila de visitas

q = deque()
q.append(s) # Q←Fila()

while len(q) > 0: # while Q .empty()=false do
    u = q.popleft()
    for v in g.vizinhos(u):
        if visitado[v] == False:
            visitado[v] = True
            d[v] = d[u] + 1
            q.append(v)


# Saida

nivel = 0
controle = True

while (controle):
	controle = False
	saida = str(nivel) + (": ")

	for i in vertices:
		if (d[i] == nivel):
			controle = True
			# Concatenar nivel com vertices do nivel, EX: 0: 1, 2, 3 
			saida += str(i) + (",")

	if (controle):
		saidaFinal = str(saida) + "\n"
		nivel += 1

	print(saidaFinal)
