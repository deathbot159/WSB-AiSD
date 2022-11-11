def do():
    try:
        n = int(input("Podaj liczbę n: "))
        if n <= 1:
            print(f"Liczba {n} nie jest liczbą pierwszą.")
            return
        for i in range(2, n):
            if i * i <= n and n % i == 0:
                print(f"Liczba {n} nie jest liczbą pierwszą.")
                return
        print(f"Liczba {n} jest liczbą pierwszą.")
    except ValueError:
        do()
    pass


if __name__ == "__main__":
    do()
