from math import log, e


class LogExp:
    """Klasa zawierająca definicję funkcji wykładniczej oraz logarytmicznej"""

    def __init__(self, a):
        """Określenie a przez konstruktor"""
        self.a = a

    def log_a(self, x):
        """logarytm o podstawie a z x"""
        try:
            return log(x) / log(self.a) if self.a > 0 and self.a != 1 else "Podano niepoprawne wartości parametru a"
        except (TypeError, ValueError):
            return "Podano niepoprawne wartości lub x nie jest w dziedzinie funkcji"

    def exp_a(self, x):
        """funkcja wykładnicza a^x"""
        try:
            return self.a ** x if self.a > 0 and self.a != 1 else "Podano niepoprawne wartości paramatru a"
        except (TypeError, ValueError):
            return "Podano niepoprawne wartości lub x nie jest w dziedzinie funkcji"


if __name__ == "__main__":
    a1 = LogExp(e)  # podanie wartości a
    a2 = LogExp(None)  # podanie wartości a
    a3 = LogExp(1)  # podanie wartości a
    log_a1 = a1.log_a(e * e)  # logarytm o podstaiwe e
    exp_a1 = a1.exp_a(2)  # funkcja wykładnicza e^x, x = 1
    print(f"{log_a1}\n{exp_a1}\n{a1.log_a(0)}\n{a2.log_a(4)}\n{a3.log_a(3)}")
