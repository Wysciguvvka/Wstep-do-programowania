import re
from datetime import datetime


def testmatch(strin):
    """Funkcja zwracająca informacje z wprowadzon"""

    pattern = r'^[A-Z]{2}[0-9]{4} [S|C] [0-9]+ [0-9]{2}:[0-9]{2} [0-9]{2}:[0-9]{2}$'
    """Pattern: r - raw string
    ^ - początek linii
    $ - koniec linii
    [A-Z] - duze litery A-Z
    {n} - ile znakow musi sie znajdowac aby byl match
    [0-9]+ - co najmniej jedna cyfra
    """

    items = strin.splitlines()
    """Oddzielenie danych: cyt. 'Każdy zestaw danych to jedna linia, ...'
    podział linie ze stringa na listę
    """
    for item in items:
        item = item.strip(' \n\r')
        # ewentualne usunięcie nowych linii (chyba mozna usunac, prawodpodobnie useless)
        if re.match(pattern, item):  # sprawdzenie czy item w liscie items pasuje do patternu
            data = item.strip().split()
            """"usunięcie spacji na początku oraz końcu (.strip()) 
            oraz oddzielenie rzeczy zawartych w zestawie danych z separatorem spacji (.split())
            """
            enter = datetime.strptime(data[3], "%H:%M")  # data wjazdu format Godzina:minuta
            leave = datetime.strptime(data[4], "%H:%M")  # data wyjazdu format Godzina:minuta
            # tutaj troche chiny:
            diff = (leave - enter).total_seconds() if enter <= leave else 86400 - (enter - leave).total_seconds()
            """Jeżeli godzina wjazdu jest mniejsza od godziny wyjazdu (np 23:59 wjazd  00:01 wyjazd),
            to od czasu 24h * 3600 sekund (86400) należy odjąć czas: (wjazd - wyjazd), ponieważ na podstawie
            danych wprowadzanych godzina przez datetime jest traktowana jako godzina z tego samego dnia +
            nie da się określić czy pojazd pokonywał daną odległość np przez 2 dni xd"""
            velocity = round(int(data[2]) * 3.6 / diff, 2)
            """prękość: data[2] - dł. trasy
            dzielona przez czas przejazdu (diff, w sekundach) -> m/s
            m/s * 3.6 => km/h
            """
            limit = 120 if data[1] == f'S' else 80
            """jeżeli samochód jest osobowy to limit 120kmh w przeciwnym razie 80"""
            over = f'M' if velocity >= limit else f'.'
            """sprawdzenie czy prędkość została przekroczona"""
            output = f'{data[0]} {over} {velocity:.2f}'
            """data[0] - rejestarcja. over - czy przekroczył prędkość (M lub .)
            velocity: prędkość zaokrąglona do 2 miejsc po przecinku (:.2f)
            """
            print(output)
            continue  # przejście do kolejnej iteracji pętli
        output = f'BLAD'  # jeżeli nie zmatchowało stringa do patternu to zwraca błąd
        print(output)  # print błąd jeżeli nie zmatchowało patternu
        # jeżeli zmatchowało pattern przechodzi do kolejnej itracji czyli print blad sie nie wykonuje


if __name__ == '__main__':
    try:
        while True:
            txt = input()
            testmatch(txt)
    except EOFError:
        pass
    """Dodatkowe uwagi
     if name == main - wykonanie, gdy plik nie jest zaimportowany jako modul
     f'text' - f-stringi
     wykorzystane: 
     regex do sprawdzenia zestawu danych
     datetime do obliczenia czasu przejazdu
    """
