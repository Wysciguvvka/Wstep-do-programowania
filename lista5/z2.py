class Prostokat:
    """klasas wyliczająca pole prostokątku na podstawie długości boków"""

    def __init__(self, a, b):
        """init"""
        self.a = a
        self.b = b

    def pole(self):
        """Obliczenie pola figury"""
        try:
            if self.a >= 0 and self.b >= 0:
                return self.a * self.b
            else:
                return "podano ujemne wartości boków"
        except (ValueError, TypeError):
            return "Podano niepoprawne wartości dla boków"


class Kwadrat(Prostokat):
    """klasa wyliczająca pole kwadratu na podstawie długości boków"""

    def __init__(self, a):
        """inicjalizacja atrybutów z klasy Prostokat"""
        Prostokat.__init__(self, a, a)


if __name__ == "__main__":
    print(Prostokat(5, 3).pole())
    print(Prostokat(5, 0.5).pole())
    print(Kwadrat(3).pole())
    print(Kwadrat(None).pole())
    print(Kwadrat(-5).pole())
