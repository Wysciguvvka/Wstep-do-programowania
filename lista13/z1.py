def format_bytes(bt):
    size = []
    for i in range(0, 3):
        b = bt // 1024 ** i
        size.append(b % 1024)
    print(f'{bt // 1024 ** 3} GB + {size[2]} MB + {size[1]} KB + {size[0]} B')


if __name__ == '__main__':
    format_bytes(9876543210)
    format_bytes(1024+1)
    format_bytes(1024 * 1024)
    format_bytes(1024 * 1024 * 1024 - 1)
    format_bytes(1024 ** 4 - 1)
