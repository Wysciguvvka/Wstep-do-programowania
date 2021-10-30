if __name__ == '__main__':
    waznosc_mleka = ('04', '11', '2021')
    karton_mleka = {}
    karton_mleka['data_waznosci'] = waznosc_mleka
    karton_mleka['waga'] = '1l'
    karton_mleka['koszt'] = 5
    karton_mleka['marka'] = 'Wadowickie'
    # print(karton_mleka.values())
    print(karton_mleka['data_waznosci'], karton_mleka['waga'], karton_mleka['koszt'], karton_mleka['marka'])
    for value in karton_mleka.values():
        print(value)
    ilosc = 6
    cena = karton_mleka['koszt']*ilosc
    print(f'Cena za {ilosc} kartonów mleka: {cena} zł')
