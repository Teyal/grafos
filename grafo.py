from typing import Iterable

class Grafo:
#    def __init__(self, v, e, w):
#        self.v = v # conjunto de vertices
#        self.e = e # conjunto de arestas
#        self.w = w # w : E -> R, a funcao que mapeia o peso de cada aresta {u,v} pertencentes a E

    def qtdVertices(self):
        return len(v)

    def qtdArestas(self):
        return len(e)

    def grau(self, v):
        return v

    def ler(self, arquivo): 
        r = open(arquivo, "r") 
        
        #entrada = input().split() #primeira entrada com vertices n
        entrada = r.readline().split()
        n = int(entrada[1])
        vertices_data = (l.split() for l in input_lines(n))  # pega os vértices com seus labels
        nomes_dict = {x: y for x, y in vertices_data}        # cria um dict com {vertice : label}

        #_ = input()  #para pular o "*edges" no arquivo
        _ = r.readline()  #para pular o "*edges" no arquivo

        peso_dict = {} #criação de dicionarios para guardar os pesos
        arestas = {}   #e as arestas
        while True:
            try:
                #entrada = input().split()
                entrada = r.readline().split()
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
    #colocar aqui a leitura do arquivo e talvez retirar o __init__

    
    def __input_lines(n: int) -> Iterable[str]:
        for _ in range(n):
            yield input()

