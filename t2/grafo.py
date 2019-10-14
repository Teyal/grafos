class Grafo:
    arestas = {}
    vertices = []
    pesos = {}
    rotulos = {}
                        #coloquei esses argumentos mas ainda nao implementei eles
    def __init__(self, direcionada = False, ponderada = False):
        arquivo = input()
        r = open(arquivo, "r")
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
            weight = int(int(entrada[2]))

            if u in arestas: # inserção {a:b}
                arestas[u]=arestas[u]+[v] # caso já exista chave
            else:
                arestas[u]=[v] #caso não há a chave ainda
            if u < v:
                peso_dict[(u,v)] = weight
            else:
                peso_dict[(v,u)] = weight

            if v in arestas: # inserção {b:a}
                arestas[v]=arestas[v]+[u] # caso já exista a chave
            else:
                arestas[v]=[u] #caso não há a chave ainda

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
        if u < v:
            return self.pesos[(u,v)]
        return self.pesos[(v,u)]

    def rotulo(self, v):
        return self.rotulos[v]

    def vizinhos(self, v):
        return self.arestas[v]
    
    def haAresta(self, u, v):
        return v in self.arestas[u]
