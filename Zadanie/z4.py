class CiagGeometryczny:
    def __init__(self, a1: float | int, q: float | int, n: int):
        self.a1 = a1
        self.q = q
        self.n = n
        """list comprehensions - utworzneie listy wyrazow ciagu
        i = 0 zwroci a1, i=1 a1 * q itd az do (n-1)
        do n-1 poniewaz liczy sie tez pierwszy wyraz do ilosci wyrazow w ciagu
        """
        self.wyrazy = [a1 * (q ** i) for i in range(0, n)]

    def add(self):
        """mnozenie ostatniego elementu z listy (-1 index) przez q"""
        self.wyrazy.append(self.wyrazy[-1] * self.q)

    def print(self):
        return self.wyrazy

    def rozmiar(self):
        return len(self.wyrazy)


if __name__ == '__main__':
    ciag = CiagGeometryczny(2, 2, 4)
    assert ciag.print() == [2, 4, 8, 16]
    assert ciag.rozmiar() == 4
    ciag.add()
    assert ciag.rozmiar() == 5
    assert ciag.print() == [2, 4, 8, 16, 32]
