import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def fit(fun, x, y):
    a, b = curve_fit(fun, x, y)
    return round(a[0], 2), fun(x, a)

def main():
    alg = sys.argv[1]
    if alg == 'randomwalk':
        fun = lambda x, a: a * np.power(x, 1/2)
        p = r'$\times \sqrt{n}$'
    elif alg == 'kruskal' or alg == 'prim':
        fun = lambda x, a: a * np.power(x, 1/3)
        p = r'$\times \sqrt[3]{n}$'
    else:
        print("Algoritmo invalido:", alg)
    arquivo = open("diametros.txt", "r")
    lines = arquivo.readlines()
    data = np.array([list(map(float, line.split())) for line in lines])
    n = data[:, 0]
    data = data[:, 1]
    a, fitted = fit(fun, n, data)
    plt.plot(n, data, 'o', label=alg.capitalize())
    plt.plot(n, fitted, label= str(a) + p, color='grey')
    plt.xlabel('Numero de vertices')
    plt.ylabel('Diametro')
    plt.legend()
    plt.savefig(alg + '.pdf')


if __name__ == "__main__":
    main()
