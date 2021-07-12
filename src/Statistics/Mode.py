from collections import Counter

def mode(num):
    try:
        num_values = len(num)
        count = Counter(num)
        get_mode = dict(count)
        test_mode = [k for k, v in get_mode.items() if v == max(list(count.values()))]
        if len(test_mode) == num_values:
            get_mode = "No mode found"
        else:
            get_mode = test_mode[0]
        return get_mode
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("Error: Check your data inputs")