from pathlib import Path
import json
import datetime


class Pamietnik:
    def __init__(self, filename):
        """Inicjalizacja klasy pamietnik"""
        self.file = Path(f"z1\\{filename}.json")
        if self.file.exists():
            with open(self.file, "r") as jsf:
                self.wpisy = json.load(jsf)
            print(f"Pomyślnie wczytano pamiętnik: {filename}")
        else:
            print(f"Utworzono nowy pamiętnik: {filename}")
            self.wpisy = []
            with open(self.file, "w") as jsf:
                json.dump(self.wpisy, jsf)

    def dodaj_wpis(self, wpis):
        """dodaje wpis do pamietnika"""
        self.wpisy.append({"data": datetime.datetime.now().strftime("%c"), "wpis": wpis})
        with open(self.file, "w") as jsf:
            json.dump(self.wpisy, jsf)

    def wyswietl_wpisy(self):
        """wyswietlenie wpisów z pamiętnika"""
        if not self.wpisy:
            print("W pliku nie ma jeszcze żadnych wpisów.")
        else:
            posortowane_wpisy = sorted(self.wpisy, key=lambda x: datetime.datetime.strptime(x['data'], '%c'))
            _tekst = "\n".join([f"{': '.join(dt.values())}" for dt in posortowane_wpisy])
            print(_tekst)


def program_pamietnik():
    """interfejs"""
    pamietnik = Pamietnik(input("Podaj nazwę pamiętnika: "))
    while True:
        opcja = input(
            "Wybierz czynność\n1. Dodaj wpis do pamiętnika \n"
            "2. Wyświetl wszystkie wpisy z pamiętnika \n3. Wyjście z programu\n")
        if opcja == "1":
            pamietnik.dodaj_wpis(input("Wpisz tekst do pamiętnika: "))
        elif opcja == "2":
            pamietnik.wyswietl_wpisy()
        elif opcja == "3":
            exit(0)
        else:
            print("Niepoprawna opcja.\n")


if __name__ == "__main__":
    program_pamietnik()
