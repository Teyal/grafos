            
# Tem 3 arquivos com formato diferente, tive que refazer para re-adaptar as 17 instancias

#def fluxoMaximo(arquivo):
#    r = open(arquivo, "r")
#    lines = r.readlines() #pra cada linha no arquivo de entrada
#    qtdVertices = lines[2].split()[2]
#    matrizCapacidades = [[0 for x in range(int(qtdVertices))] for y in range(int(qtdVertices))]

#    for line in range(5, len(lines)):
#        u = lines[line].split()[1]
#        v = lines[line].split()[2]
#        c = lines[line].split()[3]
#        matrizCapacidades[int(u)-1][int(v)-1] = int(c) # atribui a capacidade do arco
#    edmondsKarp(matrizCapacidades, int(lines[3].split()[1]), int(qtdVertices)) 


def fluxoMaximo(arquivo):
    r = open(arquivo, "r")
    lines = r.readlines() # pra cada linha no arquivo de entrada

    for line in lines:
        if "p " in line:
            qtdVertices = line.split()[2]
            matrizCapacidades = [[0 for x in range(int(qtdVertices))] for y in range(int(qtdVertices))]
        if ("a " in line) and " a " not in line:
            u = line.split()[1]
            v = line.split()[2]
            c = line.split()[3]
            matrizCapacidades[int(u)-1][int(v)-1] = int(c) # atribui a capacidade do arco
    edmondsKarp(matrizCapacidades, 1, int(qtdVertices)) 

def edmondsKarp(C, fonte, sorvedouro):
    fonte = fonte - 1
    sorvedouro = sorvedouro - 1
    n = len(C)
    F = [[0] * n for _ in range(n)]
    # Capacidade residual de u para v é C[u][v] - F[u][v]
    while True:
        caminho = BFS(C, F, fonte, sorvedouro)
        if not caminho:
            break
        # percorra ate achar a menor capacidade
        #print(u)
        u = caminho[0]
        #print(u)
        v = caminho[1]
        fluxo = C[u][v] - F[u][v]
        for i in range(len(caminho) - 2):
            u = caminho[i+1]
            v = caminho[i+2]
            fluxo = min(fluxo, C[u][v] - F[u][v])
        # percorra o caminho para atualizar o fluxo
        for i in range(len(caminho) - 1):
            u,v = caminho[i], caminho[i+1]
            F[u][v] += fluxo
            F[v][u] -= fluxo
    print('Fluxo Máximo = '+str(sum([F[fonte][i] for i in range(n)])))


def BFS(C, F, fonte, sorvedouro):
    P = [-1] * len(C)
    P[fonte] = fonte
    queue = [fonte] # inicia busca pela fonte
    while queue:
        u = queue.pop(0)
        for v in range(len(C)):
            if C[u][v] - F[u][v] > 0 and P[v] == -1:
                P[v] = u
                queue.append(v)
                if v == sorvedouro: # sorvedouro encontrado. Criar caminho aumentante
                    caminho = []
                    while True:
                        caminho.insert(0, v)
                        if v == fonte:
                            break
                        v = P[v]
                    return caminho
    return None

# FLUXO MAXIMO

fluxoMaximo('db128.gr')
