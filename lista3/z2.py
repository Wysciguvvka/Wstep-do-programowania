# import math
# import cmath
def pierwiastki():
    """funkcja do obliczania rzeczywistych miejsc zerowych funkcji kwadratowej"""
    try:
        a = float(input("Podaj współczynnik A: "))
        b = float(input("Podaj współczynnik B: "))
        c = float(input("Podaj wyraz wolny C: "))
    except ValueError:
        return "Podaj poprawną liczbę"
    if a == 0:
        return "To nie funkcja kwadratowa"
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return "brak miejsc zerowych w zobiorze liczb rzeczywistych"
    if delta > 0:
        x1 = (-1 * b + delta ** 0.5) / (2 * a)
        x2 = (-1 * b - delta ** 0.5) / (2 * a)
        return f"x1 = {x1:.2f}\nx2 = {x2:.2f}"
    x0 = (-1 * b) / (2 * a)
    return f"x0 = {x0:.2f}" if x0 != 0 else f"x0 = {abs(x0):.2f}"  # zamiana -0.00 na 0.00


if __name__ == "__main__":
    print(pierwiastki())
