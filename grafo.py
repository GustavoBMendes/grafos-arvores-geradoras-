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

        if (origem and destino) in self.vertices.keys() and (origem,destino) not in self.arestas and (destino,origem) not in self.arestas and destino != origem:
            #preencher lista de adjacencia
            self.vertices[origem].append(destino)
            self.vertices[destino].append(origem)
            #inicia com peso zero
            self.arestas.append([origem,destino,0]) 
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
        for x in grafo.vertices.keys():
            del self.vertices[x]
        for y in grafo.arestas:
            del self.arestas[y]

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
            g.arestas.append([u, v])
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


def diametro(g, vertice):
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

    while len(grafo.arestas) < n:
        origem = random.randint(0,n-1)
        destino = random.randint(0,n-1)
        grafo.adiciona_aresta(origem,destino)

    for aresta in grafo.arestas:
        aresta[2] = random.randint(0,1)

    #mst_kruskal(grafo)
    #return arvore kruskal

'''
random-tree-kruskal(n):
1 crie um grafo completo G com n vértices
2 for (u, v) in G.E
3     (u, v).w = valor aleatório entre 0 e 1
4 MST-Kruskal(G, w)
5 return a árvore produzida por MST-Kruskal
'''