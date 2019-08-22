class Grafo:
    def __init__(self, v, e, w):
        self.v = v # conjunto de vertices
        self.e = e # conjunto de arestas
        self.w = w # w : E -> R, a funcao que mapeia o peso de cada aresta {u,v} pertencentes a E


    def qtdVertices(self):
        return len(v)

    def qtdArestas(self):
        return len(e)

    def grau(self, v):
        return v

    def ler(self, arquivo): 
        r = open(arquivo, "r") 
    #colocar aqui a leitura do arquivo e talvez retirar o __init__


