def do():
    # sprawdzic czy posortowane :o
    a = [2, 3, 5, 4]
    b = [3, 6, 7, 12]
    print(f"a={all(a[i] <= a[i+1] for i in range(len(a) - 1))}\n"
          f"b={all(b[i] <= b[i+1] for i in range(len(b) - 1))}")


if __name__ == "__main__":
    do()
