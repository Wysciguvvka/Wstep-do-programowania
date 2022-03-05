class Zwierze:
    def __init__(self, imie: str, wiek: int, rodzaj: str) -> None:
        self.imie = imie
        self.wiek = wiek
        self.rodzaj = rodzaj


if __name__ == '__main__':
    z1 = Zwierze('Azor', 5, 'Pies')
    assert z1.imie == 'Azor'
    assert z1.wiek == 5
    assert z1.rodzaj == 'Pies'
    """Process finished with exit code 0 oznacza ze pomyslnie przeszlo assert.
    Gdyby bylo np wiek != 5 to zwroci AssertionError
    """
