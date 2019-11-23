import grafo as g
import random
import sys

def main():
    
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
                #test_random_walk(grafo, False)
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
                #test_random_kruskal(grafo, False)
                diametro = g.diametro(grafo)
                somador += diametro
            media = somador/500
            arquivo.write(str(n) + ' ' + str(media) + '\n')
            print('{} {}'.format(n, media))

        arquivo.close()

    elif alg == 'prim':
        for n in tamanho:
            somador = 0
            print('Gerando arvores com tamanho {}'.format(n))
            for i in range(500):
                grafo = g.grafo()
                grafo = g.random_tree_prim(n)
                test_random_prim(grafo, False)
                diametro = g.diametro(grafo)
                print(diametro)
                somador += diametro
            media = somador/500
            arquivo.write(str(n) + ' ' + str(media) + '\n')
            print('{} {}'.format(n, media))

        arquivo.close()

    else:
        print('Nome incorreto do algoritmo')

    

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

#recebe arvore gerada por kruskal e testa se esta realmente eh uma arvore
def test_random_kruskal(got, erro):

    expressao = got != erro
    mensagem = "Nao foi gerada uma arvore!"

    assert expressao, mensagem
    prefix = ' OK '

#recebe a arvore gerada por prim e testa se esta correto
def test_random_prim(got, erro):

    expressao = got != erro
    mensagem = "Nao foi gerada uma arvore!"

    assert expressao, mensagem
    prefix = ' OK '

main()