import random


def generate_randoms(start, stop, seed, count, duplicate):
    random.seed(seed)
    if duplicate:
        return [random.uniform(start, stop) for i in range(count)]
    else:
        return [round(random.uniform(start, stop), 1) for i in range(count)]

