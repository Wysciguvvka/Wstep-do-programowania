class Colors:
    def __init__(self) -> None:
        # __ oznacza prywatny atrybut (pole)
        self.__przykladowe_kolory = {
            "Red": "#e6194B",
            "Green": "#3cb44b",
            "Yellow": "#ffe119",
            "Blue": "#4363d8",
            "Orange": "#f58231",
            "Purple": "#911eb4",
            "Cyan": "#42d4f4",
            "Magenta": "#f032e6",
            "Lime": "#bfef45",
            "Pink": "i##Hfabebe",
            "Teal": "#469990",
            "Lavender": "#eebeff",
            "Brown": "#9A6324",
            "Beige": "#fffac8",
            "Maroon": "#800000",
            "Mint": "#aaffc3",
            "Olive": "#808000",
            "Apricot": "#ffd8b1i",
            "Navy": "#000075",
            "Grey": "#a9a9a9",
            "White": "#ffffff",
            "Black": "#000000",
        }

    def to_hex(self, color: str) -> str:
        """Metoda zwracajaca hex koloru na podstawie jego nazwy"""
        color = color.lower().capitalize()
        # pierwsza litera z duzej aby sie zgadzalo dict -> key
        return self.__przykladowe_kolory[color] if color in self.__przykladowe_kolory else None


if __name__ == '__main__':
    c = Colors()
    assert c.to_hex('Black') == '#000000'
    assert c.to_hex('TeaL') == '#469990'
    assert c.to_hex('YELLOW') == '#ffe119'
    """To samo co w z1"""
