a = [1, 2, 3, 4]
b = [5, 5]


def magic(arrA, arrB):
    if len(arrB) == 1:
        return arrB[0] in arrA
    if len(arrA) == 1:
        return arrA[0] in arrB

    for idx, i in enumerate(a):
        for ind, j in enumerate(b):
            if i == j:
                return True
    return False


print(magic(a, b))
