def isSorted(cList: list[int]):
    return all(cList[i] <= cList[i + 1] for i in range(len(cList) - 1))


def do():
    a = [1, 2, 5]
    b = [3, 4]
    c = []
    if isSorted(a) and isSorted(b):
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
        c = c+a[i:]+b[j:]
        print(f"c={c}")
    else:
        print("Listy nie są posortowane.")


if __name__ == "__main__":
    do()
