import matplotlib.pyplot as plt


def generate_graph(range_tentativas: int):
    """
    Function to generate the graph of the results of the ping test.
    :param range_tentativas: Number of times to perform the test
    :return: None
    """
    with open('results.csv', 'r') as file:
        hosts, times = [], []
        # Lendo o arquivo e separando os hosts e os tempos de resposta
        for line in file.readlines():
            test = line.split(',')
            hosts.append(test[0])
            times.append(test[1])
        hosts = set(hosts)  # Removendo hosts duplicados

        init_y = 0
        for host in hosts:
            times = [
                int(x) for x in times
            ]  # Convertendo os tempos de resposta para inteiros
            list_range_x = [x for x in range(1, range_tentativas + 1)]

            # Pegando os tempos de resposta desse host específico
            times_this_host = times[init_y : init_y + range_tentativas]
            # Calculando a média de tempo de resposta desse host
            average_time = sum(times_this_host) / len(times_this_host)

            # Criando os gráficos para cada host
            plt.plot(
                list_range_x,
                times_this_host,
                label=f'{host} ({average_time:.2f}ms)',
            )
            plt.title('Gráfico de tempo de resposta para os hosts')
            plt.xlabel('Tentativa')
            plt.ylabel('Time (ms)')
            plt.grid(True)  # Adicionando a grade ao gráfico

            init_y += range_tentativas
        plt.legend()  # Adicionando a legenda ao gráfico
        plt.savefig(
            'results.pdf', format='pdf', dpi=300
        )  # Salvando o gráfico em PDF
