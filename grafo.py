
## tem que pensar especificamente sobre a estrutura de dados que vai ser usada para os pesos e para as arestas
##poderia ser um dict q aponta p uma lista(vizinhos) d tuplas = (w,v) ou qlq coisa assim

class Grafo:
    arestas = {}
    vertices = {}

    def qtdVertices(self):
        return len(v)

    def qtdArestas(self):
        return len(self.arestas)

    def grau(self, v):
        return v



    def __init__(self):
        arquivo = input()
        r = open(arquivo, "r")
        ent = r.read().splitlines()
        n = int(ent[0].split()[1])

        print(ent[1:n+1])

        nomes_dict = {x: y for x, y in map(lambda e: e.split(), ent[1:n+1])}
        print("nomes = {}".format(nomes_dict))

        #eu não sei como fazer esse comprehension de cima /\

        n += 2
        peso_dict = {} #criação de dicionarios para guardar os pesos
        arestas = {}   #e as arestas
        for x in range(n,len(ent)):
            entrada = ent[x].split()
            print(entrada)
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

        self.pesos = peso_dict
        print("pesos = {}".format(peso_dict))
        self.nomes = nomes_dict
        self.arestas = arestas

g = Grafo()
print(g.qtdArestas())

#X qtdVertices():  retornr a quantidade de v ́ertices;
#X qtdArestas():  retorna a quantidade de arestas;
#grau(v):  retorna o grau do v ́erticev;
#rotulo(v):  retorna o r ́otulo do v ́erticev;
#vizinhos(v):  retorna os vizinhos do v ́erticev;
#haAresta(u, v):  se{u, v}∈E, retorna verdadeiro; se n ̃ao existir, retorna falso;
#peso(u, v):  se{u, v}∈E, retorna o peso da aresta{u, v}; se n ̃ao existir, retorna um valor infinito positivo1;
#ler(arquivo)2:  deve carregar um grafo a partir de um arquivo no formato especificado ao final deste docu-mento.
