# import math
# import sys


def pierwiastki(a, b, c):
    """funkcja do obliczania rzeczywistych miejsc zerowych funkcji kwadratowej"""
    try:
        if a == 0:
            return "To nie funkcja kwadratowa"
        delta = b ** 2 - 4 * a * c
        if delta < 0:
            return "brak miejsc zerowych w zobiorze liczb rzeczywistych"
        if delta > 0:
            x1 = (-1 * b + delta ** 0.5) / (2 * a)
            x2 = (-1 * b - delta ** 0.5) / (2 * a)
            return f"x1 = {x1:.2f}\nx2 = {x2:.2f}"
        return f"x0 = {(-1 * b) / (2 * a):.2f}"
    except TypeError:
        return "Podaj poprawną liczbę."


if __name__ == "__main__":
    print(pierwiastki(1, 0, 1))
    print(pierwiastki(1, 0, "A"))
