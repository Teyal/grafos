from typing import Iterable


vertices =[]
'''
def __input_lines__(n: int, ent: ) -> Iterable[str]:
    for _ in range(n):
        yield input()
'''

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
        ent = r.read().splitlines()
        #ent = data.
        #entrada = input().split() #primeira entrada com vertices n
        #ent = r.readline().split() #ent é entrada
        n = int(ent[0].split()[1])
        #vertices_data = [l.split() for l in ent[n]]
        #print(vertices_data)

        #vertices_data = (l.split() for l in __input_lines__(n, ent))  # pega os vértices com seus labels
        #nomes_dict = {x: y for x, y in vertices_data}        # cria um dict com {vertice : label}
        #nomes_dict = {x: y for x, y in ent[n].split() for n in range(1,n)}
        #nomes_dict = {x: y for x, y in e.split() for e in ent for }
        print(ent[1:n+1])
        #nomes_dict = {x:y for e in ent[1:n+1] for x, y in e.split()}
        #nomes_dict = {x:y for x,y in ent[1:n+1].split()}
        nomes_dict = {x: y for x, y in map(lambda e: e.split(), ent[1:n+1])}
        print(nomes_dict)

        #eu não sei como fazer esse comprehension de cima /\

        ''' parte inutil sem usar realline ou input
        #_ = input()  #para pular o "*edges" no arquivo
        _ = r.readline()  #para pular o "*edges" no arquivo
        '''

        n += 2
        peso_dict = {} #criação de dicionarios para guardar os pesos
        arestas = {}   #e as arestas
        while True:
            try:
                #entrada = input().split()
                #entrada = r.readline().split()
                entrada = ent[n].split()
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
        print(peso_dict)
        print(nomes_dict)
    #colocar aqui a leitura do arquivo e talvez retirar o __init__
