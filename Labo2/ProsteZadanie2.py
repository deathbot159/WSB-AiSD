def do():
    a = [int(v) for v in input().split()]
    found = False
    for n in a:
        if n % 2 == 1:
            found = True
            break
    print(f"{'Wszystkie liczby są parzyste' if not found else 'Znaleziono liczbe nie parzystą'}")

    # ciekawostka ,_,
    # print(all(n % 2 for n in a))


if __name__ == "__main__":
    do()
