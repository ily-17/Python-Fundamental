import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"{func.__name__} executed in {end-start:.4f} seconds")

        return result

    return wrapper


@timer
def calculate():
    total = 0
    for i in range(1000000):
        total += i

calculate()
