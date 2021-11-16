class Student:
    def __init__(self, imie, nazwisko, indeks):
        self.imie = imie
        self.nazwisko = nazwisko
        self.indeks = indeks


class Oceny(Student):
    def __init__(self, imie, nazwisko, indeks):
        super().__init__(imie, nazwisko, indeks)
        self.test = indeks

    def wyswietl_oceny(self):
        pass


if __name__ == "__main__":
    pass
