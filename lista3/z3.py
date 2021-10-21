def srednia_liczb():
    """funckja obliczająca średnią N liczb zaokrągloną za pomocą funkcji int()"""
    try:
        n = int(input("Z ilu liczb policzyć średnią: "))
    except ValueError:
        return "Podaj poprawną liczbę"
    if n <= 0:
        return "Ilość liczb musi być dodatnia"
    suma = 0
    for i in range(n):
        while True:  # while ValueError:
            try:
                x = float(input("liczba: "))
                suma += x
                break
            except ValueError:
                print("niepoprawna liczba")
    srednia = int(suma / n)
    parzystosc = f"parzysta" if srednia % 2 == 0 else f"nieparzysta"
    return f"Średnia to: {srednia} i jest ona {parzystosc}"


if __name__ == "__main__":
    print(srednia_liczb())
