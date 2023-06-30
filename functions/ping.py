import csv
from ping3 import ping

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
END = '\033[0m'


def run_ping(times: int = 100 ** 2, verbose: bool = False, *target: str):
    """
    Function to perform the ping test on hosts entered by the user.

    :param times: Number of times to perform the test (default: 100 ** 2)
    :param verbose: If the user wants to see the results of each attempt
    :param target: Hosts to be tested
    :return: Dictionary with the results of the tests
    """
    with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        result = {}
        for host in target:
            print(f'Pinging {host}...')
            result[host] = []
            for time in range(times):
                try:
                    response_time = int(ping(host, unit='ms'))
                    if response_time is None:
                        response_time = 0  # Se o host não responder, o tempo de resposta é 0, ou seja, FAIL
                    if verbose:
                        if response_time < 100 and response_time != 0:
                            print(f'Test {time + 1}: {YELLOW}{host}{END} {GREEN}OK{END} -> {response_time}ms')
                        else:
                            print(f'Test {time + 1}: {YELLOW}{host}{END} {RED}FAIL{END} -> {response_time}ms')
                except TypeError:
                    response_time = 0
                result[host].append(response_time)
                writer.writerow([host, result[host][time]])

        return result
