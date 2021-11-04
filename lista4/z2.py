def sortowanie(input_list):
    """funkcja sortująca nazwiska i wypisująca te, które mają więcej niż 5 znaków"""
    try:
        k_list = [x for x in sorted(input_list) if str(x)[0].upper() > 'K']
        print(f'Nazwiska aczynające się od liter pózniejszych w alfabecie niz K: {", ".join(k_list).title()}')
        s_list = [x for x in sorted(input_list) if len(x) > 5]
        print(f'Nazwiska posortowanie alfabetycznie, zawierające >5 znaków: {", ".join(s_list).title()}')
    except TypeError:
        print('podano niepoprawne nazwisko')


if __name__ == '__main__':
    nazwiska = ['Adamski', 'Zegar', 'Kowalski', 'limes', 'bogdan']
    sortowanie(nazwiska)
    print('---------')
    nazwiska = [3, 'Zegar', 'Kowalski', 'limes', 'bogdan']
    sortowanie(nazwiska)
