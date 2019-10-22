import random
grafo_nao_orientado = dict()

################ FUNCOES AUXILIARES ################

def adiciona_vertice(vertice):
    if vertice not in grafo_nao_orientado.keys():
        grafo_nao_orientado[vertice] = list()
        return True
    else:
        return False

def adiciona_aresta(origem, destino):

    if (origem and destino) in grafo_nao_orientado.keys() and destino not in grafo_nao_orientado[origem] and origem not in grafo_nao_orientado[destino] and destino != origem:

        grafo_nao_orientado[origem].append(destino)
        grafo_nao_orientado[destino].append(origem)

        return True

    else:
        return False

def remove_vertice(vertice):
	if vertice in grafo_nao_orientado.keys():
		del grafo_nao_orientado[vertice]
		for x in grafo_nao_orientado.keys():
			if vertice in grafo_nao_orientado[x]:
				grafo_nao_orientado[x].remove(vertice)
		return True
	else:
		return False

def print_grafo():
    for v in grafo_nao_orientado.keys():
        print('vertice {}'.format(v))
        print('adjacentes: ')
        for u in grafo_nao_orientado.get(v):
            print(u)

################ FUNCOES GRAFO ################

def busca_em_largura(vertice_inicio):
    cor = dict()    #CORES BRANCO = 1, CINZA = 2, PRETO = 3
    dist = dict() 
    pai = dict()
    fila = list()

    for v in grafo_nao_orientado.keys():
        cor[v] = 1  #BRANCO
    
    fila.append(vertice_inicio)
    cor[vertice_inicio] = 2     #CINZA
    pai[vertice_inicio] = None
    dist[vertice_inicio] = 0

    u = -1

    while len(fila):
        u = fila[0]
        del fila[0]
        for v in grafo_nao_orientado.get(u):

            if cor.get(v) == 1:
                cor[v] = 2
                dist[v] = dist[u] + 1
                pai[v] = u
                fila.append(v)

        cor[u] = 3
        
    return u, dist[u], cor

def diametro(vertice):
    a, distancia, cor = busca_em_largura(vertice)
    b, distancia, cor = busca_em_largura(a)
    return distancia

def random_tree_random_walk(n):
    i = 1
    visitado = dict()
    arestas = []

    #criar um grafo G com n vertices
    for i in range(n):
        adiciona_vertice(i)

    for u in grafo_nao_orientado.keys():
        visitado[u] = False

    u = random.choice(grafo_nao_orientado.keys())
    visitado[u] = True

    while len(arestas) < n-1:
        v = random.choice(grafo_nao_orientado.keys())
        if not visitado[v]:
            arestas.append([u, v])
            adiciona_aresta(u, v)
            visitado[v] = True
        
        u = v
    if eh_arvore(arestas) == True:
        return grafo_nao_orientado
    else:
        return False

def eh_arvore(arestas):
    if len(arestas) != len(grafo_nao_orientado.keys()) - 1:
        return False
    s = random.choice(grafo_nao_orientado.keys())
    maior, dist, cor = busca_em_largura(s)

    for v in grafo_nao_orientado.keys():
        if cor.get(v) == 1:
            return False
    return True
'''
def dfs():
    cor, tempo_inicio, tempo_fim, pai = dict(), dict(), dict(), dict()

    for u in grafo_nao_orientado.keys():
        cor[u] = 'BRANCO'
        pai[u] = None

    tempo = 0

    for u in grafo_nao_orientado.keys():
        if cor[u] == 'BRANCO':
            dfs-visit(u, tempo)

def dfs-visit(vertice, tempo):
    cor, tempo_inicio, tempo_fim = dict(), dict(), dict()

    tempo++
    cor[vertice] = 'CINZA'
    tempo_inicio[vertice] = tempo

    for v in grafo_nao_orientado.get(vertice):
        if cor[v] == 'BRANCO':
            dfs-visit(v)

    cor[vertice] = 'PRETO'
    tempo++
    tempo_fim[vertice] = tempo
'''