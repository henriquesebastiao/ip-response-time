from functions.ping import run_ping
from functions.graph import generate_graph


if __name__ == '__main__':
    targets = [x for x in input('Host(s): ').strip().split()]
    times = int(input('N° Tentativas: '))

    run_ping(times, *targets)
    generate_graph(times)
