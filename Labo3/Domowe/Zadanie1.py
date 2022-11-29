a = [-1, 100, 423, 42, 35]


def highest(arr):
    high = a[0]
    for i in range(1, len(a) - 1):
        if a[i] > high:
            high = a[i]
    return high


print(highest(a))
