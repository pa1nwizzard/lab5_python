from main import count_divisors, filtered_generator

def test_divisors():
    assert count_divisors(1) == 1
    assert count_divisors(6) == 4
    assert count_divisors(10) == 4

def test_generator_range():
    gen = filtered_generator(10, 20, max_divisors=10)
    for _ in range(20):
        num = next(gen)
        assert 10 <= num <= 20

def test_generator_divisors():
    gen = filtered_generator(10, 50, max_divisors=4)
    for _ in range(20):
        num = next(gen)
        assert count_divisors(num) <= 4