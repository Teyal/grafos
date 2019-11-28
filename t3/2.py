def hopcroftKarp(grafo):
    distancia = dict.fromkeys(grafo.vertices, float('inf'))
    vetorDeEmparelhamento = dict.fromkeys(grafo.vertices, False)

    empMax = 0
    (c, vetorDeEmparelhamento, distancia) = BFS(grafo, vetorDeEmparelhamento, distancia)
    while c:
        for x in grafo.x.keys():
            if not vetorDeEmparelhamento[x]:
                (c2, vetorDeEmparelhamento, distancia) = DFS(grafo, vetorDeEmparelhamento, x, distancia)
                if c2:
                  empMax += 1
        (c, vetorDeEmparelhamento, distancia) = BFS(grafo, vetorDeEmparelhamento, distancia)
    return (empMax, vetorDeEmparelhamento)


def BFS(grafo, vetorDeEmparelhamento, distancia):
    q = []
    for x in grafo.x.keys():
        if not vetorDeEmparelhamento[x]:
            distancia[x] = 0
            q.append(x)
        else:
            distancia[x] = float('inf')
    distancia['null'] = float('inf')
    while len(q) > 0:
        x = q.pop()
        if distancia[x] < distancia['null']:
            for y in grafo.vertices[x].getVizinhos():
                if distancia[vetorDeEmparelhamento[str(y)]] == float('inf'):
                    distancia[vetorDeEmparelhamento[str(y)]] = distancia[x] + 1
                    q.append(vetorDeEmparelhamento[str(y)])
    return (distancia['null'] != float('inf'), vetorDeEmparelhamento, distancia)


def DFS(grafo, vetorDeEmparelhamento, x, distancia):
    if x:
        for y in grafo.vertices[x].getVizinhos():
            if distancia[vetorDeEmparelhamento[str(y)]] == distancia[x] + 1:
                if DFS(grafo, vetorDeEmparelhamento, vetorDeEmparelhamento[str(y)], distancia):
                    vetorDeEmparelhamento[str(y)] = x
                    vetorDeEmparelhamento[str(x)] = y
                    return (True, vetorDeEmparelhamento, distancia)
        distancia[x] = float('inf')
        return (False, vetorDeEmparelhamento, distancia)
    return (True, vetorDeEmparelhamento, distancia)
