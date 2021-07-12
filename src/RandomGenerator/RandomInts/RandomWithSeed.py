import random


def random_with_seed(start, stop, seed):
    random.seed(seed)
    return random.randint(start, stop)