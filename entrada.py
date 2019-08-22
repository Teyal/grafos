from typing import Iterable

def input_lines(n: int) -> Iterable[str]:
    for _ in range(n):
        yield input()

entrada = input().split()

n = int(entrada[1])
#nomes_dict = {}
#for i in range(n):
#    ent = input().split()
#    rotulos[ent[0]] = ent[1]
#    e = list(rotulos.keys())

vertices_data = (l.split() for l in input_lines(n))
nomes_dict = {x: y for x, y in vertices_data}

print(nomes_dict)
print(list(nomes_dict.keys()))

_ = input()  #para pular o "*edges" no arquivo


peso_dict = {}
while True:
    try:
        entrada = input().split()
        u = entrada[0]
        v = entrada[1]
        pes = int(entrada[2])
        
       # faer uma dict d chaves q são tuplas e objetos q são os pesos 
        
    except EOFError as e:
        break

