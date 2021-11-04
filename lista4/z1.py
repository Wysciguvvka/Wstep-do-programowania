def shift(steps, input_list):
    """Funkcja przesuwająca dane w liscie"""
    if not input_list:
        return []
    try:
        if steps >= 0:
            for i in range(0, steps):
                input_list.insert(0, input_list.pop())  # usuwa ostatni element, wpisując go na miejsce 0
        else:
            for i in range(0, abs(steps)):
                input_list.append(input_list.pop(0))  # usuwa pierwszy element, dodając go na koniec listy
        return input_list
    except TypeError:
        return "Niepoprawna ilośc kroków"


if __name__ == '__main__':
    print(shift(3, []))
    print(shift(3, [1, 2, 3, 4, 5, 6]))
    print(shift(0, [1, 2, 3, 4, 5, 6]))
    print(shift(-1, [1, 2, 3, 4, 5, 6]))
    print(shift("a", [1, 2, 3, 4, 5, 6]))
