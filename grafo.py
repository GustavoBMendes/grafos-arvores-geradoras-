import random

class grafo:

    def __init__(self):
        self.arestas = []
        self.vertices = dict()
        self.visitado = []
        self.cor = []
        self.dist = dict()
        self.pai = dict()

    def adiciona_vertice(self, vertice):
        if vertice not in self.vertices.keys():
            self.vertices[vertice] = list()
            return True
        else:
            return False

    def adiciona_aresta(self, origem, destino):

        if (origem and destino) in self.vertices.keys() and destino not in self.vertices[origem] and origem not in self.vertices[destino] and destino != origem:
            self.vertices[origem].append(destino)
            self.vertices[destino].append(origem)
            self.arestas.append([origem,destino,0]) #inicia aresta com peso 0
            return True

        else:
            return False
 

    def print_grafo(self):
        print('Vertices:')
        for v in self.vertices.keys():
            print(v)
            print('Arestas')
            for u in self.vertices.get(v):
                print(u)

    def limpa_grafo(self):
        for x in self.vertices.keys():
            del self.vertices[x]
        for y in self.arestas:
            del self.arestas[y]


class union_find:

    def __init__(self):
        self.unionfind = dict()

    def make_set(self, x):
        self.unionfind[x] = list()
        self.unionfind[x].append(x)
        self.unionfind[x].append(0)
    
    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))

    def link(self, x, y):
        if self.unionfind[x][1] > self.unionfind[y][1]:
            self.unionfind[y][0] = x
        else:
            self.unionfind[x][0] = y
            if self.unionfind[x][1] == self.unionfind[y][1]:
                self.unionfind[y][1] = self.unionfind[y][1] + 1

    def find_set(self, x):
        if self.unionfind[x][0] != x:
            self.unionfind[x][0] = self.find_set(self.unionfind[x][0])
        return self.unionfind[x][0]

def random_tree_random_walk(n):    
    g = grafo()

    #criar um grafo G com n vertices
    for i in range(n):
        g.adiciona_vertice(i)

    for u in g.vertices:
        g.visitado.append(False)

    u = random.choice(g.vertices.keys())
    g.visitado[u-1] = True

    while len(g.arestas) < n-1:
        v = random.choice(g.vertices.keys())
        if not g.visitado[v-1]:
            g.adiciona_aresta(u, v)
            g.visitado[v-1] = True
        u = v

    if eh_arvore(g) == True:
        return g
    else:
        return False

def eh_arvore(grafo):
    if len(grafo.arestas) != len(grafo.vertices.keys())-1:
        return False
    s = random.choice(grafo.vertices.keys())
    maior, grafo.dist, grafo.cor = busca_em_largura(grafo, s)

    for v in grafo.vertices.keys():
        if grafo.cor[v-1] == 1: #BRANCO
            return False
    return True


def diametro(g):
    vertice = random.choice(g.vertices.keys())
    a, distancia, cor = busca_em_largura(g, vertice)
    b, distancia, cor = busca_em_largura(g, a)
    return distancia

def busca_em_largura(g, vertice_inicio):
    fila = list()
    g.cor = []
    dist = dict()
    #CORES: 1 = BRANCO, 2 = CINZA, 3 = PRETO
    for v in g.vertices.keys():
        g.cor.append(1)

    fila.append(vertice_inicio)
    g.cor[vertice_inicio] = 2
    g.pai[vertice_inicio] = None
    dist[vertice_inicio] = 0
    u = -1

    while len(fila):
        u = fila[0]
        del fila[0]
        for v in g.vertices.get(u):
            if g.cor[v] == 1:
                g.cor[v] = 2
                dist[v] = dist[u] + 1
                g.pai[v] = u
                fila.append(v)

        g.cor[u] = 3
    g.cor[vertice_inicio-1] = 3
        
    return u, dist[u], g.cor

def random_tree_kruskal(n):
    g = grafo()

    #criar um grafo G com n vertices
    for i in range(n):
        g.adiciona_vertice(i)

    for u in g.vertices.keys():
        while len(g.vertices[u]) < len(g.vertices)-1:
            origem = random.randint(0,n-1)
            destino = random.randint(0,n-1)
            g.adiciona_aresta(origem,destino)

    for aresta in g.arestas:
        aresta[2] = random.randint(0,1) #aresta(origem,destino,peso)[]
    
    a = mst_kruskal(g)
    if eh_arvore(a) == True:
        return a
    else:
        return False

def mst_kruskal(g):
    a = grafo()
    uf = union_find()
    for v in g.vertices.keys():
        uf.make_set(v)
    #ordenar arestas de forma crescente pelo peso
    g.arestas.sort(key = sortPeso)
    for aresta in g.arestas:
        if uf.find_set(aresta[0]) != uf.find_set(aresta[1]):
            a.adiciona_vertice(aresta[0])
            a.adiciona_vertice(aresta[1])
            a.adiciona_aresta(aresta[0], aresta[1])
            uf.union(aresta[0], aresta[1])
    return a

def sortPeso(val):
    return val[2]