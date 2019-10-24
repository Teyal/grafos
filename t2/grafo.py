# -*- coding: utf-8 -*-
from collections import defaultdict

class Grafo:
    arestas = {}
    vertices = []
    pesos = {}
    rotulos = {}

    def __init__(self, direcionada = False, ponderada = False):
        #arquivo = input()
        r = open("input.txt", "r")
        ent = r.read().splitlines()
        n = int(ent[0].split()[1])

        nomes_dict = {int(x): y for x, y in map(lambda e: e.split(), ent[1:n+1])}
        self.vertices = list(nomes_dict.keys())
        n += 2
        peso_dict = {} #criação de dicionarios para guardar os pesos
        arestas = {}   #e as arestas
        for x in range(n,len(ent)):
            entrada = ent[x].split()
            u = int(entrada[0])
            v = int(entrada[1])
            

            if u in arestas: # inserção {a:b}
                arestas[u]=arestas[u]+[v] # caso já exista chave
            else:
                arestas[u]=[v] #caso não há a chave ainda

            if not direcionada:
                if v in arestas: # inserção {b:a}
                    arestas[v]=arestas[v]+[u] # caso já exista a chave
                else:
                    arestas[v]=[u] #caso não há a chave ainda
            
            if ponderada:
                weight = int(int(entrada[2]))
                if u < v:
                    peso_dict[(u,v)] = weight
                else:
                    peso_dict[(v,u)] = weight

        if ponderada:
            self.pesos = peso_dict
        self.rotulos = nomes_dict
        self.arestas = arestas

    def qtdVertices(self):
        return len(self.vertices)

    def qtdArestas(self):
        return len(self.arestas)

    def grau(self, v):
        return len(self.arestas[v])

    def peso(self, u, v):
        if ponderada:
            if u < v:
                return self.pesos[(u,v)]
            return self.pesos[(v,u)]

    def rotulo(self, v):
        return self.rotulos[v]

    def vizinhos(self, v):
        return self.arestas[v]
    
    def haAresta(self, u, v):
        return v in self.arestas[u]

    def transposta(self):
        #def invert_graph(edges: Dict[Node, List[Node]]):
        invertido = defaultdict(lambda: [])
        for u, destinos in self.arestas.items():
            for v in destinos:
                if u not in invertido[v]:
                    invertido[v].append(u)
        return dict(invertido)
