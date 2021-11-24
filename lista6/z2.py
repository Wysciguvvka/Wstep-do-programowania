from hashlib import md5
import re


class Uzytkownik:
    """Klasa zawierajca informacje o uzytkowniku"""

    def __init__(self, username, fname, lname, email, password):
        """inicjalizacja"""
        self.username = username
        _pattern = r"^[\w*-\.]*@([\w*-\.]*)[\.]([\w]{2,4})$"
        if not re.match(_pattern, email):
            print('Podano niepoprawny email')
        self.email = email
        self.fname = fname
        self.lname = lname
        self.__password = md5(password.encode()).hexdigest()  # prywatny atrybut
        self.proby_logowania = 0

    def opisz_uzytkownika(self):
        """Metoda opisująca użytkownika"""
        print(f'Nazwa użytkownika: {self.username}\nEmail: {self.email}'
              f'\nImię i nazwisko: {self.fname.title()} {self.lname.title()}'
              f'\nPróby logowania: {self.proby_logowania}'
              f'\n{"Jesteś administratorem." if isinstance(self, Admin) else ""}')

    def pozdrow_uzytkownika(self):
        """Metoda wyświetlająca spersonalizowane pozdrowienie użytkownika"""
        print(f'Witam {self.fname.title()} {self.lname.title()}, pozdrawiam')

    def dodaj_proby_logowania(self, val):
        """Metoda dodająca próby logowania"""
        try:
            if val >= 0 and isinstance(val, int):
                self.proby_logowania += val
            else:
                print("Nieopoprawna ilość prób")
        except TypeError:
            print("Nieopoprawna ilość prób")

    def zresetuj_proby_logowania(self):
        """Metoda resetująca próby logowania"""
        self.proby_logowania = 0

    def zaloguj(self, password):
        """Metoda umożliwiająca zalogowanie się na konto"""
        self.proby_logowania += 1
        print('Zalogowano' if md5(password.encode()).hexdigest() == self.__password else 'podano niepoprawne hasło')


class Admin(Uzytkownik):
    """Klasa zawiarające informacje o administratorach"""

    def __init__(self, username, fname, lname, email, password):
        """Inicjalizacja atrybutów"""
        super().__init__(username, fname, lname, email, password)
        # self.przywileje = Przywileje().przywileje
        self.przywileje = ['Może dodać post', 'Może usunąć post', 'Może zablokować użytkownika',
                           'Może odblokować użytkownika']

    def pokaz_przywileje(self):
        """Wyświetlenie przywilejów administratora"""
        print(f"Przywileje: {', '.join([przywilej for przywilej in self.przywileje])}")


class Przywileje:
    """Klasa zawierająca przywileje administratora"""

    def __init__(self, user):
        """Inicjalizacja klasy przywileje"""
        self.przywileje = user.przywileje

    def pokaz_przywileje(self):
        """Wyświetlenie przywilejów administratora"""
        print(f"Przywileje: {', '.join([przywilej for przywilej in self.przywileje])}")


if __name__ == '__main__':
    user1 = Uzytkownik('nazwa', 'imie', 'nazwisko', 'email@pwr.edu.pl', 'haslo')
    user2 = Uzytkownik('nazwa', 'imie', 'nazwisko', 'email@test', 'haslo')
    print('----')
    user1.pozdrow_uzytkownika()
    user1.opisz_uzytkownika()
    user1.dodaj_proby_logowania(-5)
    user1.dodaj_proby_logowania('a')
    user1.dodaj_proby_logowania(7)
    user1.zaloguj('haslo1')
    user1.zaloguj('haslo')
    user1.opisz_uzytkownika()
    print('----')
    user2.dodaj_proby_logowania(5)
    user2.opisz_uzytkownika()
    user2.zresetuj_proby_logowania()
    user2.opisz_uzytkownika()
    print('----')
    admin1 = Admin('nazwa', 'imie', 'nazwisko', 'email1@pwr.edu.pl', 'haslo')
    admin1.zaloguj('haslo')
    przywileje = Przywileje(admin1)
    przywileje.pokaz_przywileje()
    admin1.dodaj_proby_logowania(-5)
    admin1.dodaj_proby_logowania(3)
    admin1.pokaz_przywileje()
    admin1.opisz_uzytkownika()