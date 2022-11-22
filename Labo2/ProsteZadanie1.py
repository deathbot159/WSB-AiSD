def do():
    try:
        x = float(input("Podaj liczbe a: "))
        if (x**2) % 2 == 0:
            print(x / 2)
        else:
            print(x * 2)
    except ValueError:
        do()


if __name__ == "__main__":
    do()
