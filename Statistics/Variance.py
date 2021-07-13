import statistics as stats


def variance(num):
    try:
        c = stats.variance(num)
        return c
    except (IndexError) or (ValueError):
        return None