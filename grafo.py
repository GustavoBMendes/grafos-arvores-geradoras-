grafo_nao_orientado = dict()

def adiciona_vertice(vertice):
    if vertice not in grafo_nao_orientado.keys():
        grafo_nao_orientado[vertice] = list()
        print('Inserido vertice {}'.format(vertice))
        return True
    else:
        return False

def adiciona_aresta(origem, destino):

    if (origem and destino) in grafo_nao_orientado.keys() and destino not in grafo_nao_orientado[origem] and origem not in grafo_nao_orientado[destino]:

        grafo_nao_orientado[origem].append(destino)
        grafo_nao_orientado[destino].append(origem)

        grafo_nao_orientado[origem] = list(set(grafo_nao_orientado[origem]))
        grafo_nao_orientado[destino] = list(set(grafo_nao_orientado[destino]))
        
        print('Aresta inserida ligando o vertice {} ao vertice {}'.format(origem, destino))

        return True

    else:
        return False

def busca_em_largura(vertice_inicio):
    cor, dist, pai, fila, aresta, arvore = dict(), dict(), dict(), list(), dict(), dict()

    for v in grafo_nao_orientado.keys:
        cor[v] = 'BRANCO'
    
    fila.append(vertice_inicio)
    cor[vertice_inicio] = 'CINZA'
    pred[vertice_inicio] = None
    dist[vertice_inicio] = 1

    while len(fila):
        u = fila.pop(0)
        for v in grafo_nao_orientado.get(u):

            if cor.get(v) == 'BRANCO':
                cor[v] = 'CINZA'
                dist[v] = dist[u] + 1
                pred[v] = u
                fila.append(v)
        cor[u] = 'PRETO'
        
    return cor, pred, aresta, dist, arvore