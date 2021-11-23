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
        print(f'Nazwa użytkownika: {self.username}\nEmail: {self.email}'
              f'\nImię i nazwisko: {self.fname.title()} {self.lname.title()}')

    def pozdrow_uzytkownika(self):
        print(f'Witam {self.fname.title()} {self.lname.title()}, pozdrawiam')

    def dodaj_probe_logowania(self):
        self.proby_logowania += 1

    def zresetuj_proby_logowania(self):
        self.proby_logowania = 0

    def zaloguj(self, password):
        self.proby_logowania += 1
        print('Zalogowano' if md5(password.encode()).hexdigest() == self.__password else 'podano niepoprawne hasło')


class Admin(Uzytkownik):
    def __init__(self, username, fname, lname, email, password):
        super().__init__(username, fname, lname, email, password)
        self.przywileje = Przywileje()  # ????????


class Przywileje:
    def __init__(self):
        self.przywileje = ['Może dodać post', 'Może usunąć post', 'Może zablokować użytkownika',
                           'Może odblokować użytkownika']

    def pokaz_przywileje(self):
        print(f"Przywileje: {', '.join([przywilej for przywilej in self.przywileje])}")


if __name__ == '__main__':
    user1 = Uzytkownik('nazwa', 'imie', 'nazwisko', 'email@pwr.edu.pl', 'haslo')
    user2 = Uzytkownik('nazwa', 'imie', 'nazwisko', 'email@email', 'haslo')
    user1.pozdrow_uzytkownika()
    user1.opisz_uzytkownika()
    user1.zaloguj('haslo')
    user1.zaloguj('haslo1')
    user1.opisz_uzytkownika()
    admin1 = Admin('nazwa', 'imie', 'nazwisko', 'email1@pwr.edu.pl', 'haslo')
    Przywileje().pokaz_przywileje()
