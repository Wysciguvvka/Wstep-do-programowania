if __name__ == '__main__':
    try:
        liczba = float(input("podaj liczbę: "))
        print(f'podana liczba to {liczba}')
    except ValueError:
        print(f'nie podano poprawnej liczby')
