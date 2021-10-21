# z1.
def cena_biletu():
    """Funckja obliczająca cenę biletu na podstawie wieku"""
    try:
        wiek = int(input("podaj swój wiek: "))
    except ValueError:
        return "niepoprawny wiek"
    cena = f"10zł" if wiek < 19 or wiek > 61 else f"20zł"
    return f"cena biletu to: {cena}"


if __name__ == "__main__":
    print(cena_biletu())
