def suma():
    try:
        inp = int(input("Podaj liczbe: "))
        tak = list(str(inp))
        ret = 0
        for n in tak:
            ret += int(n)
        return ret
    except ValueError:
        print("Podano nieprawidłową wartość.")
        suma()


print(suma())
