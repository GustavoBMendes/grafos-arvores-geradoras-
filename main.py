import grafo as g
import random
import sys

def main():
    '''
    g.adiciona_vertice(1)
    g.adiciona_vertice(2)
    g.adiciona_vertice(3)
    g.adiciona_vertice(4)
    g.adiciona_vertice(5)
    g.adiciona_vertice(6)
    g.adiciona_vertice(7)
    g.adiciona_vertice(8)
    g.adiciona_aresta(1,2)
    g.adiciona_aresta(1,7)
    g.adiciona_aresta(1,6)
    g.adiciona_aresta(1,8)
    g.adiciona_aresta(2,5)
    g.adiciona_aresta(2,3)
    g.adiciona_aresta(3,4)
    g.print_grafo()
    maior, dist, cor = g.busca_em_largura(4)
    print('Vertice com a maior distancia = {}'.format(maior));
    test_bfs(maior, 8)
    
    distancia = g.diametro(1)
    test_diametro(distancia, 4)
    for v in g.grafo_nao_orientado.keys():
        g.remove_vertice(v)
    print('removido')
    g.print_grafo()
    tree = g.random_tree_random_walk(10)
    test_random_walk(tree, g.grafo_nao_orientado)
    '''
    alg = sys.argv[1]
    tamanho = [250,500,750,1000,1250,1500,1750,2000]
    arquivo = open("diametros.txt", "w")
    if alg == 'randomwalk':
        for n in tamanho:
            somador = 0
            print('Gerando arvores com tamanho {}'.format(n))
            for i in range(500):
                grafo = g.grafo()
                grafo = g.random_tree_random_walk(n)
                test_random_walk(grafo, False)
                diametro = g.diametro(grafo)
                somador += diametro
            media = somador/500
            arquivo.write(str(n) + ' ' + str(media) + '\n')
            print('{} {}'.format(n, media))

        arquivo.close()

    elif alg == 'kruskal':
        for n in tamanho:
            somador = 0
            print('Gerando arvores com tamanho {}'.format(n))
            for i in range(500):
                grafo = g.grafo()
                grafo = g.random_tree_kruskal(n)
                test_random_kruskal(grafo, False)
                diametro = g.diametro(grafo)
                somador += diametro
            media = somador/500
            arquivo.write(str(n) + ' ' + str(media) + '\n')
            print('{} {}'.format(n, media))

        arquivo.close()

    else:
        print('Nome incorreto do algoritmo')
    
    grafo = g.random_tree_kruskal(250)
    test_random_kruskal(grafo, False)
#recebe o diametro da arvore e testa se esta correto
def test_diametro(got, expected):

    expressao = got == expected
    mensagem = "Diametro incorreto!"

    assert expressao, mensagem
    prefix = ' OK '
    print("%s got 'diametro': %s expected: %s" % (prefix, repr(got), repr(expected)))

#recebe o vertice de maior distancia do bfs e o valor da distancia
def test_bfs(got, expected):

    expressao = got == expected
    mensagem = "BFS incorreto!"

    assert expressao, mensagem
    prefix = ' OK '
    print("%s got 'vertice': %s expected: %s" % (prefix, repr(got), repr(expected)))


#recebe o grafo da arvore e testa se esta correto
def test_random_walk(got, erro):

    expressao = got != erro
    mensagem = "Nao foi gerada uma arvore!"

    assert expressao, mensagem
    prefix = ' OK '
    #print("%s got 'random tree': %s erro: %s" % (prefix, repr(got), repr(erro)))

#recebe o grafo da arvore e testa se esta correto
def test_random_kruskal(got, erro):

    expressao = got != erro
    mensagem = "Nao foi gerada uma arvore!"

    assert expressao, mensagem
    prefix = ' OK '

main()