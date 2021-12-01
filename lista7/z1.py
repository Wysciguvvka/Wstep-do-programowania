import moj_modul

# from moj_modul import *
# import moj_modul as user
# from moj_modul import Admin

if __name__ == '__main__':
    admin1 = moj_modul.Admin('nazwa', 'imie', 'nazwisko', 'email1@pwr.edu.pl', 'haslo')
    # admin1 = Admin('nazwa', 'imie', 'nazwisko', 'email1@pwr.edu.pl', 'haslo')
    # admin1 = user.Admin('nazwa', 'imie', 'nazwisko', 'email1@pwr.edu.pl', 'haslo')
    # admin1 = Admin('nazwa', 'imie', 'nazwisko', 'email1@pwr.edu.pl', 'haslo')
    admin1.zaloguj('haslo')
    admin1.dodaj_proby_logowania(-5)
    admin1.dodaj_proby_logowania(3)
    admin1.pokaz_przywileje()
    admin1.opisz_uzytkownika()
    admin1.dodaj_proby_logowania(-5)
    admin1.dodaj_proby_logowania(3)
    admin1.pokaz_przywileje()
    admin1.opisz_uzytkownika()
