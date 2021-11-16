class Prostokat:
    """klasas wyliczająca pole prostokątku na podstawie długości boków"""

    def __init__(self, a, b):
        """init"""
        self.a = a
        self.b = b


class Kwadrat(Prostokat):
    """klasas wyliczająca pole kwadratu na podstawie długości boków"""

    def __init__(self, a, b):
        Prostokat.__init__(self, a, b)
        self.a = a
        self.b = b

    def pole(self):
        print(self.a)


if __name__ == "__main__":
    Kwadrat.pole(1, 2)
