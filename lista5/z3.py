class Student:
    """Klasa z informacjami o studencie"""

    def __init__(self, imie, nazwisko, indeks):
        """init"""
        if not indeks.isdecimal() or len(indeks) != 6:
            print("podano niepoprawny index")
        else:
            self.imie = imie
            self.nazwisko = nazwisko
            self.indeks = indeks
            self.oceny = {
                "przedmiot1": None,
                "przedmiot2": None,
                "przedmiot3": None
            }


class Informacje(Student):
    def __init__(self, imie, nazwisko, indeks):
        super().__init__(imie, nazwisko, indeks)

    def wyswietl_oceny(self):
        """Wyswietlenie ocen studenta"""
        print(f"Oceny studenta: {self.oceny}")

    def dodaj_oceny(self, przedmiot, ocena):
        """dodaje oceny"""
        if not self.oceny[przedmiot]:
            self.oceny[przedmiot] = ocena
            print(f"Dodano nową ocenę {self.oceny[przedmiot]}")
        else:
            print("Ocena już istnieje.")

    def zmien_oceny(self, przedmiot, ocena):
        """Zmienia oceny studenta"""
        if self.oceny[przedmiot]:
            stara_ocena = self.oceny[przedmiot]
            self.oceny[przedmiot] = ocena
            print(f"Zmieniono ocenę {stara_ocena} na {self.oceny[przedmiot]}")
        else:
            print(f"Zanim zmienisz ocenę z {self.oceny[przedmiot]} dla studenta {self.indeks} musisz ją dodać.")


if __name__ == "__main__":
    student0 = Informacje("stud", "stud", "asd")
    student1 = Informacje("student1", "nazwisko1", "123456")
    student2 = Informacje("x", "y", "654321")
    Informacje.wyswietl_oceny(student1)
    Informacje.dodaj_oceny(student1, "przedmiot1", 3.0)
    Informacje.zmien_oceny(student1, "przedmiot2", 4.0)
    Informacje.dodaj_oceny(student1, "przedmiot2", 4.0)
    Informacje.dodaj_oceny(student1, "przedmiot3", 5.0)
    Informacje.wyswietl_oceny(student1)
    Informacje.zmien_oceny(student1, "przedmiot3", 5.5)
    Informacje.wyswietl_oceny(student1)
    Informacje.wyswietl_oceny(student2)