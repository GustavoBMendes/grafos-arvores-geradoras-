from collections import deque
import random

#constantes
branco = "BRANCO"
cinza = "CINZA"
preto = "PRETO"

class grafo:

    def __init__(self):
        self.arestas = []
        self.vertices = dict()

    def adiciona_vertice(self, vertice):
        if vertice not in self.vertices.keys():
            self.vertices[vertice] = list()
            return True
        else:
            return False

    def adiciona_aresta(self, aresta):

        if aresta.destino not in self.vertices[aresta.origem] and aresta.origem not in self.vertices[aresta.destino] and aresta.destino != aresta.origem:
            self.vertices[aresta.origem].append(aresta.destino)
            self.vertices[aresta.destino].append(aresta.origem)
            self.arestas.append(aresta) 
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

class Aresta:
    def __init__(self,u,v):
        self.origem = u
        self.destino = v
        self.w = -1

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
    visitado = []

    #criar um grafo G com n vertices
    for i in range(n):
        g.adiciona_vertice(i)

    for u in g.vertices:
        visitado.append(False)

    u = random.randint(0, n-1)
    visitado[u] = True

    while len(g.arestas) < n-1:
        v = random.choice(g.vertices.keys())
        if not visitado[v]:
            g.adiciona_aresta(Aresta(u, v))
            visitado[v] = True
        u = v

    if eh_arvore(g) == True:
        return g
    else:
        return False

def eh_arvore(grafo):
    cor = []
    tam = len(grafo.arestas)
    if tam != len(grafo.vertices.keys())-1:
        return False
    s = random.randint(0,len(grafo.vertices.keys())-1)
    maior, dist, cor = busca_em_largura(grafo, s)

    for v in grafo.vertices.keys():
        if cor[v] == branco: 
            return False
    return True


def diametro(g):
    vertice = random.choice(g.vertices.keys())
    a, distancia, cor = busca_em_largura(g, vertice)
    b, distancia, cor = busca_em_largura(g, a)
    return distancia

def busca_em_largura(g, vertice_inicio):
    cor = []
    dist = dict()
    pai = dict()
    
    for v in g.vertices.keys():
        cor.append(branco)

    fila = deque([])
    fila.append(vertice_inicio)
    cor[vertice_inicio] = cinza
    pai[vertice_inicio] = None
    dist[vertice_inicio] = 0
    u = -1

    while len(fila):
        u = fila.popleft()
        for v in g.vertices.get(u):
            if cor[v] == branco:
                cor[v] = cinza
                dist[v] = dist[u] + 1
                pai[v] = u
                fila.append(v)

        cor[u] = preto
    cor[vertice_inicio-1] = preto
        
    return u, dist[u], cor

def random_tree_kruskal(n):
    g = grafo()

    #criar um grafo completo G com n vertices
    for i in range(n):
        g.adiciona_vertice(i)

    for u in g.vertices.keys():
        while len(g.vertices[u]) < len(g.vertices)-1:
            origem = random.randint(0,n-1)
            destino = random.randint(0,n-1)
            g.adiciona_aresta(Aresta(origem,destino))

    for aresta in g.arestas:
        aresta.w = random.randint(0,1) #aresta(origem,destino,peso)[]
    
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
        a.adiciona_vertice(v)
    #ordenar arestas de forma crescente pelo peso
    g.arestas.sort(key = sortPeso)
    for aresta in g.arestas:
        if uf.find_set(aresta.origem) != uf.find_set(aresta.destino):
            a.adiciona_aresta(aresta)
            uf.union(aresta.origem, aresta.destino) 
    return a

def sortPeso(val):
    return val.w

def random_tree_prim(n):
    g = grafo()

    #criar um grafo completo G com n vertices
    for i in range(n):
        g.adiciona_vertice(i)

    for u in g.vertices.keys():
        while len(g.vertices[u]) < len(g.vertices)-1:
            origem = random.randint(0,n-1)
            destino = random.randint(0,n-1)
            g.adiciona_aresta(Aresta(origem,destino))

    for aresta in g.arestas:
        aresta.w = random.randint(0,1) #aresta(origem,destino,peso)[]

    s = random.randint(0,n-1)
    return mst_prim(g, s)

def mst_prim(g, s):
    pai = dict()
    chave = []

    for u in g.vertices:
        chave.append(-1)
        pai[u] = None

    chave[s] = 0
    q = g.vertices.copy()

    while len(q) > 0:
        u = min(q)
        del q[u]
        print(len(q))
        for v in g.vertices.get(u):
            peso = get_peso(g.arestas, u, v)
            if v in q and peso < chave[v]:
                pai[v] = u
                chave[v] = peso

    return g

def get_peso(arestas, u, v):
    for i in arestas:
        if (i.origem == u and i.destino == v) or (i.origem == v and i.destino == u):
            return i.w
    print('Aresta nao encontrada')