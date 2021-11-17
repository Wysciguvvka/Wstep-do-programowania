class Informacje:
    """Klasa z informacjami o studencie"""

    def __init__(self, imie, nazwisko, indeks):
        """init"""
        if not str(indeks).isdecimal() or len(indeks) != 6:
            print("podano niepoprawny indeks")
            # exit(1)
        else:
            self.imie = imie
            self.nazwisko = nazwisko
            self.indeks = indeks
            self.oceny = {
                "przedmiot1": 0,
                "przedmiot2": 0,
                "przedmiot3": 0
            }


class Student(Informacje):
    def __init__(self, imie, nazwisko, indeks):
        super().__init__(imie, nazwisko, indeks)

    def wyswietl_dane(self):
        """Wyswietlenie informacji o studencie"""
        ocenianie = "\n".join([f"{przedmiot}: {ocena}" for przedmiot, ocena in self.oceny.items()])
        print(f"Student o ideksie {self.indeks}:\nImie: {self.imie}\n"
              f"Nazwisko: {self.nazwisko}\nOceny studenta:\n{ocenianie}")

    def wyswietl_oceny(self):
        """Wyswietlenie ocen studenta"""
        ocenianie = "\n".join([f"{przedmiot}: {ocena}" for przedmiot, ocena in self.oceny.items()])
        #print(f"Oceny studenta {self.indeks}: {self.oceny}")
        print(f"Oceny studenta {self.indeks}:\n{ocenianie}")

    def dodaj_oceny(self, przedmiot, ocena):
        """Dodanie nowej oceny do przedmiotu"""
        try:
            if not self.oceny[przedmiot]:
                self.oceny[przedmiot] = ocena
                print(
                    f"Dodano nową ocenę {self.oceny[przedmiot]} z przedmiotu {przedmiot} "
                    f"dla studenta o indeksie {self.indeks}")
            else:
                print(f"Ocena już istnieje z przedmiotu {przedmiot} "
                      f"dla studenta o indeksie {self.indeks} już istnieje.")
        except KeyError:
            print(f"Podano niepoprawny przedmiot: {przedmiot} podczas dodawania oceny")

    def zmien_oceny(self, przedmiot, ocena):
        """Zmiana istniejącej oceny"""
        try:
            if self.oceny[przedmiot]:
                stara_ocena = self.oceny[przedmiot]
                self.oceny[przedmiot] = ocena
                print(f"Zmieniono ocenę {stara_ocena}  z przedmiotu {przedmiot} na {self.oceny[przedmiot]}")
            else:
                print(f"Zanim zmienisz ocenę z {przedmiot} dla studenta {self.indeks} musisz ją dodać.")
        except KeyError:
            print(f"Podano niepoprawny przedmiot: {przedmiot} podczas próby zmiany oceny")


if __name__ == "__main__":
    student0 = Student("stud", "stud", "asd")
    student1 = Student("student1", "nazwisko1", "123456")
    student2 = Student("x", "y", "654321")
    print('----')
    Student.wyswietl_oceny(student1)
    print('----')
    Student.zmien_oceny(student1, "przedmiot1", 4.0)
    print('---')
    Student.dodaj_oceny(student1, "przedmiot1", 3.0)
    Student.dodaj_oceny(student1, "przedmiot2", 4.0)
    Student.dodaj_oceny(student1, "przedmiot3", 5.0)
    Student.dodaj_oceny(student1, "przedmiot5", 5.0)
    print('----')
    Student.wyswietl_oceny(student1)
    print('----')
    Student.zmien_oceny(student1, "przedmiot3", 5.5)
    print('----')
    Student.wyswietl_oceny(student1)
    Student.wyswietl_oceny(student2)
    print('----')
    Student.wyswietl_dane(student1)
    # Informacje.wyswietl_oceny(student0)
