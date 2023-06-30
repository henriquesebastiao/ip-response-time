import csv
from ping3 import ping


def run_ping(times: int = 100 ** 2, *target: str):
    """
    Function to perform the ping test on hosts entered by the user.

    :param times: Number of times to perform the test (default: 100 ** 2)
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
                    # print(f'{host} -> {response_time}ms')
                except TypeError:
                    response_time = 0
                result[host].append(response_time)
                writer.writerow([host, result[host][time]])

        return result
