def general_median(a):
    a.sort()
    if (len(a) % 2) == 0:
        mid_right = int(len(a) // 2)
        mid_left = mid_right - 1
        result = (a[mid_left] + a[mid_right]) / 2
    elif (len(a) % 2) == 1:
        result = a[int((len(a) - 1) // 2)]
    return result


