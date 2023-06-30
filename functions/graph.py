import matplotlib.pyplot as plt


def generate_graph(x_range: int):
    """
    Function to generate the graph of the results of the ping test.
    :param x_range: Number of times to perform the test
    :return: None
    """
    with open('results.csv', 'r') as file:
        hosts, times = [], []
        for line in file.readlines():
            test = line.split(',')
            hosts.append(test[0])
            times.append(test[1])
        hosts = set(hosts)

        init_y = 0
        for host in hosts:
            range_tentativas = x_range
            x_range = [x for x in range(x_range)]
            times = [int(x) for x in times]

            # Pegando os tempos de resposta desse host
            times_this_host = times[init_y:init_y + range_tentativas]
            # Calculando a média de tempo de resposta desse host
            average_time = sum(times_this_host) / len(times_this_host)

            # Criando o gráfico
            plt.plot(x_range, times_this_host)
            plt.title(f'Gráfico de {host}')
            plt.xlabel('Tentativa')
            plt.ylabel('Time (ms)')
            plt.legend([f'Média: {average_time:.2f}ms'])
            plt.grid(True)
            plt.show()

            init_y += range_tentativas
