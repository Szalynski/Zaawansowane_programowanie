def parzyste(liczby):
    nowe_liczby = []
    for liczba in liczby:
        if liczba%2 == 0:
            nowe_liczby.append(liczba)
    return nowe_liczby