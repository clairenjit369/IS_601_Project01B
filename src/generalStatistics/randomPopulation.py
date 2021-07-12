from random import randint


def random_population(a, b, c):
    data = []
    for i in range(c):
        data.append(randint(a, b))
    return data
