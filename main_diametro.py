import diametro as d

def main():
    d.adiciona_vertice(1)
    d.adiciona_vertice(2)
    d.adiciona_vertice(3)
    d.adiciona_vertice(4)
    d.adiciona_vertice(5)
    d.adiciona_vertice(6)
    d.adiciona_vertice(7)
    d.adiciona_vertice(8)
    d.adiciona_aresta(1,2)
    d.adiciona_aresta(1,7)
    d.adiciona_aresta(1,6)
    d.adiciona_aresta(1,8)
    d.adiciona_aresta(2,5)
    d.adiciona_aresta(2,3)
    d.adiciona_aresta(3,4)

    d.print_grafo()

    #busca em largura iniciando no vertice 4
    maior = d.busca_em_largura(4)
    print(maior);
    test_bfs(maior, (7, 4))
    
    distancia = d.diametro(1)
    test_diametro(distancia, 4)

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