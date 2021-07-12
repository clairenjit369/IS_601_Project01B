def general_mode(a):
    a.sort()
    count = 0
    frequency = 0
    for i in range(len(a)):
        if i > 0 and a[i] == a[i-1]:
            count += 1
            if count > frequency:
                frequency = count
                result = a[i]
        elif i > 0 and a[i] != a[i-1]:
            count = 1
        else:
            count = 1
    return result




