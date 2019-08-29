from collections import deque

'''
arquivo = input()
n = int(input())

g = Grafo()
g.ler(arquivo)
'''

s = 2 # trocar por: s = g.vertice[n]
q = deque()
q.append(s) # Q←Fila()
vertices = [0,1,2,4]

visitado = {x:False for x in vertices} # Cv←false ∀v ∈ V
niveis = [[s]]


'''o resultado deve ser: [ [s]  [N(s)] [N(N(s))]]'''
visitado[n] = True # Cs←true

while len(q) > 0: # while Q .empty()=false do
    u = q.popleft()
    for v in g.vizinhos(u):
        if visitado[v] == False:
            visitado[v] = True
            Dv = Du + 1
            q.append(v)

'''
while

1Cv←false∀v∈V
2Dv←∞∀v∈V
3Av←null∀v∈V// configurando o vértice de origem
4Cs←true
5Ds←0// preparando fila de visitas
6Q←Fila()
7Q.enqueue(s)// propagação das visitas
8whileQ .empty()=falsedo
9u←Q.dequeue()
10foreach v ∈ N(u) do
11ifCv=falsethen
12Cv←true
13Dv←Du+1
14Av←u
15Q.enqueue(v)
return (D,A)
'''
