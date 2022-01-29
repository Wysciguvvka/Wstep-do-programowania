import re
from datetime import datetime


def testmatch(strin):
    pattern = r'^[A-Z]{2}[0-9]{4} [S|C] [0-9]+ [0-9]{2}:[0-9]{2} [0-9]{2}:[0-9]{2}$'
    items = strin.splitlines()
    for item in items:
        item = item.strip(' \n\r')
        if re.match(pattern, item):  # sprawdzenie czy item w liscie items pasuje do patternu
            data = item.strip().split()
            enter = datetime.strptime(data[3], "%H:%M")  # data wjazdu format Godzina:minuta
            leave = datetime.strptime(data[4], "%H:%M")  # data wyjazdu format Godzina:minuta
            diff = (leave - enter).total_seconds() if enter <= leave else 86400 - (enter - leave).total_seconds()
            velocity = round(int(data[2]) * 3.6 / diff, 2)
            limit = 120 if data[1] == f'S' else 80
            over = f'M' if velocity >= limit else f'.'
            output = f'{data[0]} {over} {velocity:.2f}'
            print(output)
            continue
        output = f'BLAD'
        print(output)


if __name__ == '__main__':
    try:
        while True:
            txt = input()
            testmatch(txt)
    except EOFError:
        pass