import time
from functools import reduce

# Линейный конгруэнтный генератор (без random!)
def lcg(seed=1):
    a = 1664525
    c = 1013904223
    m = 2**32

    while True:
        seed = (a * seed + c) % m
        yield seed


# Подсчёт количества делителей числа
def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2 if i != n // i else 1
    return count


# Генератор чисел в диапазоне с фильтрацией
def filtered_generator(start, end, max_divisors, seed=1):
    gen = lcg(seed)

    while True:
        num = next(gen)
        num = start + num % (end - start + 1)

        if count_divisors(num) <= max_divisors:
            yield num


# Использование map / filter / reduce
def process_numbers(numbers):
    # filter: оставляем только чётные
    filtered = list(filter(lambda x: x % 2 == 0, numbers))

    # map: возводим в квадрат
    mapped = list(map(lambda x: x**2, filtered))

    # reduce: сумма
    total = reduce(lambda a, b: a + b, mapped, 0)

    return mapped, total


# Демонстрация
if __name__ == "__main__":
    gen = filtered_generator(10, 100, max_divisors=6)

    numbers = [next(gen) for _ in range(10)]
    print("Сгенерированные числа:", numbers)

    mapped, total = process_numbers(numbers)
    print("После map (квадраты чётных):", mapped)
    print("Сумма (reduce):", total)