from datetime import datetime, time


class Restauracja:
    """Klasa zawierająca informacje o restauracji"""

    def __init__(self, nazwa, typ, klienci=0):
        """inicjalizacja restauracji"""
        self.nazwa = nazwa
        self.typ = typ
        self.klienci = klienci
        self.godziny = {  # domyslne godziny otwarcia
            'Monday': [time(7, 0), time(18, 30)],
            'Tuesday': [time(7, 0), time(18, 30)],
            'Wednesday': [time(7, 0), time(18, 30)],
            'Thursday': [time(7, 0), time(18, 30)],
            'Friday': [time(7, 0), time(18, 30)],
            'Saturday': [time(7, 0), time(18, 30)],
            'Sunday': None
        }

    def opis_restauracji(self):
        """Metoda wyświetlająca informacje o restauracji"""
        print(f"{self.nazwa}, {self.typ}, {self.klienci}")

    def __jest_otwarta(self, data, dzien):
        """prywatna metoda sprawdzająca, czy restauracja jest otwarta"""
        return True if self.godziny[dzien] and self.godziny[dzien][0] <= data <= self.godziny[dzien][1] else False

    def jest_otwarta(self):
        """Publiczna metoda sprawdzająca, czy restauracja teraz jest otwarta"""
        now = datetime.now().time()
        dzien = datetime.today().strftime("%A")
        otwarcie = f'Restauracja \"{self.nazwa}\" jest otwarta' if \
            self.__jest_otwarta(now, dzien) else f'Restauracja \"{self.nazwa}\" jest zamknięta'
        print(otwarcie)

    def ustaw_liczbe_obsluzonych_klietow(self, ilosc):
        """Metoda ustawiajca liczbę obsłużonych klientów"""
        if isinstance(ilosc, int) and ilosc >= 0:
            self.klienci = ilosc
        else:
            print('Niepoprawna ilość klientów')

    def dodaj_liczbe_obsluzonych_klientow(self, ilosc):
        """Metoda dodajca n obsłużonych klientów"""
        try:
            if isinstance(ilosc, int) and ilosc >= 0:
                self.klienci += ilosc
            else:
                print('Niepoprawna ilość klientów')
        except (TypeError, ValueError):
            print('Niepoprawna ilość klientów')

    def zmien_godziny_otwarcia(self, nowe_godziny):
        """Metoda zmieniająca godziny otwarcia restauracji"""
        try:
            for key, values in nowe_godziny.items():
                if key not in self.godziny.keys():
                    print('podano niepoprawny dzień')
                    break
                if values and (len(values) != 2 or any(not isinstance(value, time) for value in values)):
                    print('Podano niepoprawne godziny')
                    break
            else:
                self.godziny.update(nowe_godziny)
        except TypeError:
            print('Podano niepoprawne godziny')

    def wyswietl_godziny_otwarcia(self):
        _dni = {
            'Monday': 'Poniedziałek',
            'Tuesday': 'Wtorek',
            'Wednesday': 'Środa',
            'Thursday': 'Czwartek',
            'Friday': 'Piątek',
            'Saturday': 'Sobota',
            'Sunday': 'Niedziela'
        }
        godziny_otwarcia = f''
        for key, value in self.godziny.items():
            godziny_otwarcia += f'{_dni[key]}: {" - ".join([val.strftime("%H:%M") for val in value])}\n' if value \
                else f'{_dni[key]} - Zamknięte\n'
        print(godziny_otwarcia)


class Lodziarnia(Restauracja):
    """Klasa zawierajca informacje o lodziarni"""

    def __init__(self, nazwa, typ):
        """inicjalizacja klasy lodziarnia"""
        super().__init__(nazwa, typ)
        self.smaki = []

    def dodaj_smaki(self, *args):
        """metoda dodająca smaki do katalogu lodzianri"""
        for arg in args:
            if arg not in self.smaki:
                self.smaki.append(arg)
            else:
                print(f'Lody o smaku \"{arg}\" są już na liście')

    def usun_smaki(self, *args):
        """Metoda usuwajća smaki z katalogu lodziarni"""
        for arg in args:
            if arg in self.smaki:
                self.smaki.remove(arg)
                print(f'Usunięto lody o smaku: {arg}')
            else:
                print(f'Lodów o smaku {arg} nie ma na liście.')

    def wyswietl_smaki(self):
        """Metoda wyświetląca smaki lodów"""
        if self.smaki:
            lista_smakow = ', '.join([smak for smak in self.smaki])
            print(f'Smaki lodów: {lista_smakow}')
        else:
            print('Lodziarnia nie ma uzupełnionych lodów.')


if __name__ == '__main__':
    restauracja1 = Restauracja('Restauracja1', 'Typ1')
    restauracja2 = Restauracja('Restauracja2', 'Typ2')
    restauracja3 = Restauracja('Restauracja3', 'Typ3')
    print(restauracja1.typ, restauracja2.nazwa, restauracja3.klienci)
    print('-----')
    restauracja1.opis_restauracji()
    restauracja1.jest_otwarta()
    restauracja1.dodaj_liczbe_obsluzonych_klientow(23)
    restauracja1.opis_restauracji()
    restauracja1.ustaw_liczbe_obsluzonych_klietow(0)
    restauracja1.wyswietl_godziny_otwarcia()
    restauracja1.jest_otwarta()

    zmienione_godziny = {'Wednesday': [time(10, 00), time(13, 30)], 'Sunday': [time(8, 00), time(14, 30)]}
    # zmienione_godziny = {'Wednesday': '1'}
    restauracja1.zmien_godziny_otwarcia(zmienione_godziny)

    restauracja1.wyswietl_godziny_otwarcia()
    restauracja1.jest_otwarta()
    restauracja1.ustaw_liczbe_obsluzonych_klietow(-1)
    restauracja1.opis_restauracji()
    print('-----')
    lodziarnia1 = Lodziarnia('Lodziarnia1', 'Typ1')
    lodziarnia1.wyswietl_smaki()
    lodziarnia1.dodaj_smaki('smak1', 'smak2')
    lodziarnia1.wyswietl_smaki()
    lodziarnia1.usun_smaki('smak1')
    lodziarnia1.usun_smaki('smak3')
    lodziarnia1.wyswietl_smaki()
    lodziarnia1.opis_restauracji()
