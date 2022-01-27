import re
from datetime import datetime


def testmatch(strin):
    if re.match(r"^[A-Z]{2}[0-9]{4} [S|C] [0-9]+ [0-9]{2}:[0-9]{2} [0-9]{2}:[0-9]{2}$", strin):
        data = strin.split()
        enter = datetime.strptime(data[3], "%H:%M")
        leave = datetime.strptime(data[4], "%H:%M")
        # chinszczyzna:
        """ 
        prawdzenie czy data wjazdu jest mniejsza niz data wyjazdu jezeli nie, to odejmuje 24h*3600
        na podstawie podanych dnaych nie da sie sprawdzic czy pojazd przejezdza trase >24h xd
        """
        diff = (leave - enter).total_seconds() if enter <= leave else 86400 - (enter - leave).total_seconds()
        velocity = round(int(data[2]) * 3.6 / diff, 2)  # m/s * 3.6 => km/h
        limit = f'M' if velocity > 120 else f'.'
        return f'{data[0]} {limit} {diff:.2f}'
    return f'BLAD'


if __name__ == '__main__':
    print(testmatch('DW3123 S 1500 21:00 21:01'))
    print(testmatch('DW3123 . 90.00'))
    print(testmatch('DW3113 S 5500 23:59 00:01'))
    print(testmatch('GD3124 C 3500 00:00 00:02'))
    print(testmatch('DX1234 DROP TABLE USERS S 5500 00:01 00:2'))
