import moj_modul

modul = __import__('moj_modul')
# from moj_modul import *
# import moj_modul as user
# from moj_modul import Admin

if __name__ == '__main__':
    admin1 = moj_modul.Admin('nazwa', 'imie', 'nazwisko', 'email1@pwr.edu.pl', 'haslo')
    admin2 = modul.Admin('nazwa', 'imie', 'nazwisko', 'email1@pwr.edu.pl', 'haslo')
    # admin1 = Admin('nazwa', 'imie', 'nazwisko', 'email1@pwr.edu.pl', 'haslo')
    # admin1 = user.Admin('nazwa', 'imie', 'nazwisko', 'email1@pwr.edu.pl', 'haslo')
    # admin1 = Admin('nazwa', 'imie', 'nazwisko', 'email1@pwr.edu.pl', 'haslo')
    admin1.pokaz_przywileje()
    admin1.opisz_uzytkownika()
    print('---------')
    admin2.pokaz_przywileje()
    admin2.opisz_uzytkownika()
