def do():
    try:
        a = int(input("Podaj liczbę a: "))
        b = int(input("Podaj liczbę b: "))

        if (a == 0) and (b == 0):
            print("Nieskończenie wiele rozwiązań")
        elif (a == 0) and (b != 0):
            print("Brak rozwiązań")
        elif (a != 0) and (b == 0):
            print("x=0")
        else:
            print(f"x={(b / a) * -1}")

    except ValueError:
        do()
    pass


if __name__ == "__main__":
    do()
