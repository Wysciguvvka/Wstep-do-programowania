if __name__ == '__main__':
    with open('zad1.txt', 'a',
              encoding='utf-8') as file:  # parametr a tworzy plik, jeżeli plik nie istnieje oraz zapisuje dane na koncu pliku
        while True:
            s = input('podaj tekst: ')
            if s == '':  # s.replace(' ', '') żeby spacja liczyła się jako pusta linijka
                break
            file.write(f'{s}\n')
