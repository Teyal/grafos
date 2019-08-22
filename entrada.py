from typing import Iterable

def input_lines(n: int) -> Iterable[str]:
    for _ in range(n):
        yield input()

entrada = input().split() #primeira entrada com vertices n
n = int(entrada[1])
vertices_data = (l.split() for l in input_lines(n))  # pega os vértices com seus labels
nomes_dict = {x: y for x, y in vertices_data}        # cria um dict com {vertice : label}

_ = input()  #para pular o "*edges" no arquivo

peso_dict = {} #criação de dicionarios para guardar os pesos
arestas = {}   #e as arestas
while True:
    try:
        entrada = input().split()
        u = entrada[0]
        v = entrada[1]
        weight = int(entrada[2])

        if u in arestas: # inserção {a:b}
            arestas[u]=arestas[u]+[v] # caso já exista chave
        else:
            arestas[u]=[v] #caso não há a chave ainda
        
        
        if v in arestas: # inserção {b:a}
            arestas[v]=arestas[v]+[u] # caso já exista a chave
        else:
            arestas[v]=[u] #caso não há a chave ainda
        
    except EOFError as e:
        break
print(arestas)
