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
    g.adiciona_aresta(6,5)
    g.adiciona_aresta(2,5)
    g.adiciona_aresta(2,3)
    g.adiciona_aresta(3,4)

    #g.print_grafo()

    maior = g.busca_em_largura(1)

    print(maior)

main()