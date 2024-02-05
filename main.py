import sys

from functions.graph import generate_graph
from functions.ping import run_ping

if __name__ == '__main__':
    # Verificando se o usuário quer ver os resultados de cada tentativa
    if len(sys.argv) > 1:
        if sys.argv[1] == '--verbose' or sys.argv[1] == '-v':
            verbose = True
        else:
            verbose = False
    else:
        verbose = False

    targets = [x for x in input('Host(s): ').strip().split()]
    times = int(input('N° Tentativas: '))

    run_ping(times, verbose, *targets)
    generate_graph(times)
