class Prostokat:
    def __init__(self, dlugosc: float | int, szerokosc: float | int):
        if dlugosc <= 0 or szerokosc <= 0:
            # upewnienie sie, ze wartosci sa dodatnie
            raise ValueError
        self.a = dlugosc
        self.b = szerokosc

    def pole(self):
        return self.a * self.b

    def obwod(self):
        return 2 * (self.a + self.b)


if __name__ == '__main__':
    p = Prostokat(10, 2)
    assert p.pole() == 20
    assert p.obwod() == 24
