# z1.
def cena_biletu():
    """Funckja obliczająca cenę biletu na podstawie wieku"""
    try:
        wiek = int(input("podaj swój wiek: "))
    except ValueError:
        return "niepoprawny wiek"
    # cena = f"10zł" if not 19 < wiek < 61 else f"20zł"
    if 19 < wiek < 61:
        cena = f"20zł"
    elif wiek >= 61:
        cena = f"15zł"
    else:
        cena = f"10zł"
    return f"cena biletu to: {cena}"


if __name__ == "__main__":
    print(cena_biletu())
