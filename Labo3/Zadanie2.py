import time

a = [2, 2, 3, 4, 5, 6, 6, 7, 7, 12]


def binary_search(arr, low, high, search):
    start = int(time.time_ns())
    end = None
    if high >= low:
        middle = (low + high) // 2
        if arr[middle] == search:
            return middle
        elif arr[middle] > search:
            end = int(time.time_ns())
            print(f"Wykonano w {end - start}ns")
            return binary_search(arr, low, middle - 1, search)
        else:
            end = int(time.time_ns())
            print(f"Wykonano w {end - start}ns")
            return binary_search(arr, middle + 1, high, search)
    else:
        end = int(time.time_ns())
        print(f"Wykonano w {end - start}ns")
        return -1


print(binary_search(a, 0, len(a) - 1, 2))
