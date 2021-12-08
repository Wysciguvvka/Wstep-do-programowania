if __name__ == '__main__':
    try:
        with open('zad1.txt', 'r', encoding='utf-8') as file:
            data = file.read()
    except FileNotFoundError:
        print('plik nie istnieje')
    else:
        print(data)



