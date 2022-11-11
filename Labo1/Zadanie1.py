def do():
    try:
        a = int(input("Podaj liczbe: "))
        if (a % 3) == 0 or (a % 5) == 0:
            print(f"Liczba \"{a}\" {'jest podzielna przez 3 i 5' if (((a % 3)+(a % 5))==0) else 'jest podzielna przez 3' if ((a % 3)==0) else 'jest podzielna przez 5' if ((a % 5)==0) else ''}")
        else:
            print(f"Liczba \"{a}\" nie jest podzielna przez 3 ani przez 5")
    except ValueError:
        do()
    pass


if __name__ == "__main__":
    do()
