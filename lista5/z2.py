class Prostokat:
    """klasas wyliczająca pole prostokątku na podstawie długości boków"""

    def __init__(self, a, b):
        """init"""
        self.a = a
        self.b = b

    def pole(self):
        """Obliczenie pola figury"""
        return self.a * self.b


class Kwadrat(Prostokat):
    """klasas wyliczająca pole kwadratu na podstawie długości boków"""

    def __init__(self, a, b):
        """init"""
        Prostokat.__init__(self, a, b)
        self.b = self.a


if __name__ == "__main__":
    print(Prostokat(5, 2).pole())
    print(Kwadrat(5, 1).pole())
