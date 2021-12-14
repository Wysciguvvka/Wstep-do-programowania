if __name__ == '__main__':
    with open('zad1.txt', 'a') as file:
        while True:
            s = input('podaj tekst: ')
            if not s:
                break
            file.write(f'{s}\n')
