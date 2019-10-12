import grafo as g

def main():
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

    maior = g.busca_em_largura(4)
    print(maior);
    test_bfs(maior, (7, 4))
    
    distancia = g.diametro(1)
    test_diametro(distancia, 4)

    for v in g.grafo_nao_orientado.keys():
        g.remove_vertice(v)

    print('removido')
    g.print_grafo()

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
    mensagem = "Diametro incorreto!"

    assert expressao, mensagem
    prefix = ' OK '
    print("%s got 'vertice, distancia': %s expected: %s" % (prefix, repr(got), repr(expected)))


main()