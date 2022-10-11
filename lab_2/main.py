from zad_1 import wypisz_imiona
from zad_2 import mnozenie_1
from zad_2 import mnozenie_2
from zad_3 import parzyste
from zad_4 import co_drugie

wypisz_imiona(["Adam","Ola","Marek","Jan","Kasia"]) #zad_1

liczby = mnozenie_1([1,5,4,2,7]) #zad_2a
print(liczby);

liczby2 = mnozenie_2([1,5,4,2,7]) #zad_2a
print(liczby2);

#zad 3 liczba pażysta
liczby3 = [x for x in range(0,11)]
print(liczby3)
liczby3 = parzyste(liczby3)
print(liczby3)

#zad_4 co druga liczba
liczby4 = [x for x in range(5,15)]
print(liczby4)
liczby4 = co_drugie(liczby4)
print(liczby4)


