from hashlib import md5


class Uzytkownik:
    def __init__(self, username, fname, lname, email, password, bdate):
        self.username = username
        self.email = email
        self.fname = fname
        self.lname = lname
        self.__password = md5(password.encode()).hexdigest()  # prywatny atrybut
        self.bdate = bdate
        self.proby_logowania = 0

    def opisz_uzytkownika(self):
        pass

    def pozdrow_uzytkownika(self):
        print(f'Witam {self.fname.title()} {self.lname.title()}, pozdrawiam')

    def zaloguj(self, password):
        self.proby_logowania += 1
        if md5(password.encode()).hexdigest() == self.__password:
            print('Zalogowano')
        else:
            print('podano niepoprawne hasło')


if __name__ == '__main__':
    user1 = Uzytkownik('nazwa', 'imie', 'nazwisko', 'email', 'haslo', 'urodziny')
    user1.pozdrow_uzytkownika()
    user1.opisz_uzytkownika()
    user1.zaloguj('haslo')
    user1.opisz_uzytkownika()
