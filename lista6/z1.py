from datetime import datetime, time


class Restauracja:
    def __init__(self, nazwa, typ, klienci=0):
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
        print(f"{self.nazwa}, {self.typ}, {self.klienci}")

    def __jest_otwarta(self, data, dzien):
        """prywatna metoda sprawdzająca, czy restauracja jest otwarta"""
        return True if self.godziny[dzien] and self.godziny[dzien][0] <= data <= self.godziny[dzien][1] else False

    def jest_otwarta(self):
        """Publiczna metoda sprawdzająca, czy restauracja teraz jest otwarta"""
        now = datetime.now().time()
        dzien = datetime.today().strftime("%A")
        otwarcie = f'Restauracja \"{self.nazwa}\" jest otwarta' if \
            self.__jest_otwarta(now, dzien) and dzien != 'Sunday' else f'Restauracja \"{self.nazwa}\" jest zamknięta'
        print(otwarcie)

    def ustaw_liczbe_obsluzonych_klietow(self, ilosc):
        if isinstance(ilosc, int):
            self.klienci = ilosc
        else:
            print('Niepoprawna ilość klientów')

    def dodaj_liczbe_obsluzonych_klientow(self, ilosc):
        try:
            if isinstance(ilosc, int) and ilosc > 0:
                self.klienci += ilosc
            else:
                print('Niepoprawna ilość klientów')
        except (TypeError, ValueError):
            print('Niepoprawna ilość klientów')

    def zmien_godziny_otwarcia(self, godziny):
        self.godziny.update(godziny)

    def wyswietl_godziny_otwarcia(self):
        dni = {
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
            godziny_otwarcia += f'{dni[key]}: {" - ".join([val.strftime("%H:%M") for val in value])}\n' if value \
                else f'{dni[key]} - Zamknięte\n'
        print(godziny_otwarcia)


class Lodziarnia(Restauracja):
    def __init__(self, nazwa, typ):
        super().__init__(nazwa, typ)
        self.smaki = []

    def dodaj_smaki(self, *args):
        for arg in args:
            if arg not in self.smaki:
                self.smaki.append(arg)
            else:
                print(f'Lody o smaku \"{arg}\" są już na liście')

    def usun_smaki(self, *args):
        for arg in args:
            self.smaki.remove(arg)

    def wyswietl_smaki(self):
        if self.smaki:
            lista_smakow = ', '.join([smak for smak in self.smaki])
            print(f'Smaki lodów: {lista_smakow}')
        else:
            print('Lodziarnia nie ma uzupełnionych lodów.')


if __name__ == '__main__':
    restauracja1 = Restauracja('Restauracja1', 'Typ1')
    restauracja2 = Restauracja('Restauracja2', 'Typ2')
    restauracja3 = Restauracja('Restauracja3', 'Typ3')
    restauracja1.opis_restauracji()
    restauracja1.jest_otwarta()
    lodziarnia1 = Lodziarnia('Lodziarnia1', 'Typ1')
    lodziarnia1.wyswietl_smaki()
    lodziarnia1.dodaj_smaki('smak1', 'smak2')
    lodziarnia1.wyswietl_smaki()
    lodziarnia1.usun_smaki('smak1')
    lodziarnia1.wyswietl_smaki()
    lodziarnia1.opis_restauracji()
    restauracja1.wyswietl_godziny_otwarcia()
    nowe_godziny = {'Sunday': [time(10, 00), time(16, 30)]}
    restauracja1.zmien_godziny_otwarcia(nowe_godziny)
    restauracja1.wyswietl_godziny_otwarcia()
