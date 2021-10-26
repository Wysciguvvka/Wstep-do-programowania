# import math
# import sys


def pierwiastki(a, b, c):
    """funkcja do obliczania rzeczywistych miejsc zerowych funkcji kwadratowej"""
    if a == 0:
        return "To nie funkcja kwadratowa"
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return "brak miejsc zerowych w zobiorze liczb rzeczywistych"
    if delta > 0:
        x1 = (-1 * b + delta ** 0.5) / (2 * a)
        x2 = (-1 * b - delta ** 0.5) / (2 * a)
        x1 = x1 if x1 != 0 else 0  # Usunięcie 'negative zero'
        x2 = x2 if x2 != 0 else 0  # Usunięcie 'negative zero'
        return f"x1 = {x1:.2f}\nx2 = {x2:.2f}"
    x0 = (-1 * b) / (2 * a)
    x0 = x0 if x0 != 0 else 0  # Usunięcie 'negative zero'
    return f"x0 = {x0:.2f}"


if __name__ == "__main__":
    a1 = b1 = c1 = 0  # Usunięcie 'can be undefined' warning
    try:
        a1 = float(input("Podaj współczynnik A: "))
        b1 = float(input("Podaj współczynnik B: "))
        c1 = float(input("Podaj wyraz wolny C: "))
    except ValueError:
        print("Podaj poprawną liczbę.")
        # sys.exit()
        exit(1)
    print(pierwiastki(a1, b1, c1))
