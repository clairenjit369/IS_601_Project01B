import random
import numpy as np


def generate_randoms(start, stop, seed, count, duplicate):
    random.seed(seed)
    np.random.seed(seed)
    if duplicate:
        return np.random.randint(start, stop, size=count)
    else:
        return [random.randint(start, stop) for r in range(count)]
