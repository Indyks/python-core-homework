from ex2 import fetcher
import time
CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов
    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        def wrapper_too(*args, **kwargs):
            total_time = 0
            for i in range(num):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                lead_time = end - start
                print("Прогон №", i + 1, " выполнен за ", lead_time)
                total_time += lead_time
            print("Среднее время выполнения: ", total_time / num)
        return wrapper_too
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
