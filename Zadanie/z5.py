from __future__ import annotations


class Czas:
    def __init__(self, godzin: str, minut: str = None):
        """Inicjalizacja klasy, minut jest opcjonalnm argumentem"""
        if not minut:
            """Tutaj troche chiny = jezeli nie ma minut to split tam gdzie spacja i wziecie
             odpowiednich wartosci. jezeli minuty nie zostaly podane, lista bedzie za krotka
             , wiec sprawdzenie dlugosci listy zesplitowanych elementow i jezeli < 2 to 
             ustaiwenie na 0
             """
            godziny = godzin.split()
            godzin = f'{godziny[0].strip()} h'
            minut = f'{godziny[2].strip()} min' if 2 < len(godziny) else f'0 min'
        """Konwersja na typu liczbowego"""
        self.godzin = int(godzin.split('h')[0])
        self.minut = int(minut.split('min')[0])

        if self.minut >= 60:
            """opncjonalne sprawdzenie, czy minuty sa poprawne
            godziny moga byc dowolna liczba
            (w tresci zadania nie ma zadnego sprawdzania wiec mozna usunac)
            """
            raise ValueError

    def dodaj(self, czas: Czas) -> Czas:
        """ (self.minut + czas.minut) // 60 dzieli sume minut na 60 z zaookragleniem w dol
        (w ten sposob wychodzi liczba godzin z sumy minut np: 25 min i 40 min da 65-> 65//60 zwroci 1h)
        % 60 - modulo 60 ( 60 minut w godzine, duh)
        """
        godziny = self.godzin + czas.godzin + (self.minut + czas.minut) // 60
        minuty = (self.minut + czas.minut) % 60
        return Czas(f'{godziny} h {minuty} min')

    def odejmij(self, czas: Czas) -> Czas:
        """analgoiczne  to tego co wyzej
        nie wiem jak to ma wygladac poprawnie, wiec zrobilem
        roznice pomiedzy przedzialami czasowymi np:
        pomiedzy 12h 50 min i 12h 00 min jest 59 minut roznicy.
        analogicznie z 12h 00 min i 12h 50 min.
        """

        godziny = abs(self.godzin - czas.godzin - (abs(self.minut - czas.minut)) // 60)
        minuty = abs(self.minut - czas.minut) % 60  # zakladamy, ze podane minuty sa dodatnie
        return Czas(f'{godziny} h {minuty} min')

    def pomnoz(self, ile: int) -> Czas:
        godziny = self.godzin * ile + (self.minut * ile // 60)
        minuty = (self.minut * ile) % 60
        return Czas(f'{godziny} h {minuty} min')

    def __str__(self) -> str:
        return f'{self.godzin} h {self.minut} min'

    def __add__(self, other: Czas) -> Czas:
        return self.dodaj(other)

    def __sub__(self, other: Czas) -> Czas:
        return self.odejmij(other)

    def __mul__(self, other: int) -> Czas:
        return self.pomnoz(other)

    def __eq__(self, other: Czas) -> bool:
        """dodatek do dodatkow - porownanie czy
        czasy zawieraja jednakowe godziny i minuty"""
        return self.minut == other.minut and self.godzin == other.godzin


if __name__ == '__main__':
    cz1 = Czas('1 h', '25 min')
    cz2 = Czas('2 h 55 min')

    assert cz1.dodaj(cz2) == Czas('4 h 20 min')
    assert cz1.odejmij(cz2) == Czas('1 h 30 min')
    assert cz1.pomnoz(3) == Czas('4 h 15 min')

    assert cz1 + cz2 == Czas('4 h 20 min')
    assert cz1 - cz2 == Czas('1 h 30 min')
    assert cz1 * 3 == Czas('4 h 15 min')
