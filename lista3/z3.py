def srednia_liczb(*args):
    """funckja obliczająca średnią N liczb zaokrągloną za pomocą funkcji int()"""
    suma = 0
    for arg in args:
        suma += arg
    srednia = int(suma / len(args))
    parzystosc = f"parzysta" if srednia % 2 == 0 else f"nieparzysta"
    return f"Zaokrąglona średnia to: {srednia} i jest ona {parzystosc}"


if __name__ == "__main__":
    print(srednia_liczb(1,2,3,4,5,6,7,8,9))
