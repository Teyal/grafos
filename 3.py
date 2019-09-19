#teste

#vertices = [[7 for x in range(2)] for y in range(10)]
vertices = [1, 2, 3, 4, 5, 6]
arestas = [[1, 2],[1, 3],[2, 3],[4, 5],[4, 6],[5, 6]]
pesos = [3, 6, 12, 1, 2, 9]
contadorDoNumero = 0

def haCicloEuleriano(arestas):
  for x in vertices:
    for i in arestas:
      for j in i :
        if j == x:
          global contadorDoNumero
          contadorDoNumero += 1 #wtf
    if contadorDoNumero < 2:
      return 0
    if contadorDoNumero % 2 == 0:
      contadorDoNumero = 0
    else:
      return 0
  return 1;

print(haCicloEuleriano(arestas))

