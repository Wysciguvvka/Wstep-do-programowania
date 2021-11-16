from math import log, e


class LogExp:
    """Klasa zawierająca definicję funkcji wykładniczej oraz logarytmicznej"""

    def __init__(self, a):
        """Określenie a przez konstruktor"""
        self.a = a

    def log_a(self, x):
        """logarytm o podstawie a z x"""
        try:
            return log(x) / log(self.a) if self.a > 0 and self.a != 1 else None
        except (TypeError, ValueError):
            return None

    def exp_a(self, x):
        """funkcja wykładnicza a^x"""
        try:
            return self.a ** x if self.a > 0 and self.a != 1 else None
        except (TypeError, ValueError):
            return None


if __name__ == "__main__":
    a1 = LogExp(e)
    log_a1 = a1.log_a(e)  # logarytm o podstaiwe e z e
    exp_a1 = a1.exp_a(1)  # funkcja wykładnicza e^x, x = 1
    print(log_a1, exp_a1, a1.log_a(0))
