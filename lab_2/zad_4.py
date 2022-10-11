def co_drugie(liczby):
    nowe_liczby = []
    for idx,liczba in enumerate(liczby):
        if idx%2 == 0:
            nowe_liczby.append(liczba)
    return nowe_liczby