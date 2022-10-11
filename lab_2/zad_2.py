def mnozenie_1(liczby):
    nowa_liczba = []
    for liczba in liczby:
        nowa_liczba.append(liczba*2)
    return nowa_liczba

def mnozenie_2(liczby):
    nowa_liczba = [liczba*2 for liczba in liczby]
    return nowa_liczba