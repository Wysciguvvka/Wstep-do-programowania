import re
from datetime import datetime


def testmatch(strin):
    pattern = r'([A-Z]{2}[0-9]{4} [S|C] [0-9]+ [0-9]{2}:[0-9]{2} [0-9]{2}:[0-9]{2})'
    output = ''
    # items = list(filter(None, re.split(pattern, strin)))
    items = strin.splitlines()
    for item in items:
        item = item.strip(' \n\r')
        if re.match(pattern, item):
            data = item.strip().split()
            enter = datetime.strptime(data[3], "%H:%M")
            leave = datetime.strptime(data[4], "%H:%M")
            diff = (leave - enter).total_seconds() if enter <= leave else 86400 - (enter - leave).total_seconds()
            velocity = round(int(data[2]) * 3.6 / diff, 2)  # m/s * 3.6 => km/h
            limit = 120 if data[1] == f'S' else 80
            over = f'M' if velocity >= limit else f'.'
            output += f'{data[0]} {over} {velocity:.2f}'
            continue
        output += f'BLAD'
    print(output)


if __name__ == '__main__':
    txt = input()
    testmatch(txt)
