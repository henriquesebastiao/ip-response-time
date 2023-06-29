from ping3 import ping


def run_ping(times: int = 100 ** 2, *target: str):
    """
    Function to perform the ping test on hosts entered by the user.

    :param times: Number of times to perform the test (default: 100 ** 2)
    :param target: Hosts to be tested
    :return: Dictionary with the results of the tests
    """
    response_times = {}
    for host in target:
        response_times[host] = []
        for time in range(times):
            response_times[host].append(ping(host))

    return response_times
