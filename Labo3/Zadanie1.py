import time

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 4


def getIdx(arr: list, search) -> int:
    start = int(time.time_ns())
    for idx, n in enumerate(arr):
        if n == search:
            end = int(time.time_ns())
            print("Wykonano w "+str(end-start)+"ns")
            return idx
    end = int(time.time_ns())
    print("Wykonano w "+str(end-start)+"ns")
    return -1
    # return a.index(x) if x in a else -1


print(getIdx(a, x))
