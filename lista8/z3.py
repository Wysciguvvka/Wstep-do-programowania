if __name__ == '__main__':
    try:
        with open('zad1.txt', 'r') as file:
            data = file.read()
    except FileNotFoundError:
        print('plik nie istnieje')
    else:
        print(f'Ilość znaków: {len(data)}')
        text = input('wpisz szukaną frazę: ')
        print(f'Podana fraza pojawia się {data.count(text)} raz/y')
