import requests
from Zad_1 import wypisz
from zad_2 import mnozenie
from zad_3 import parzysta
from zad_4 import porownaj
from zad_5 import zawiera
from zad_6 import listmerger

#Zadanie 1
wynik = wypisz("Tomasz","Adamczyk")
print(wynik)

#Zadanie 2
print(mnozenie(5,3))

#Zadanie 3
liczba = parzysta(3)
print("Liczba jest parzysta") if liczba else print("Liczba jest nieparzysta")

#Zadanie 4
print(porownaj(2,3,4))
print(porownaj(3,5,9))

#Zadanie 5
print(zawiera([1,2,3,4,5],3))
print(zawiera([1,2,3,4,5],6))

#Zadanie 6
print(listmerger([1,2,3,4,5],[4,5,6,7,8]))

#Zadanie 7
response_API = requests.get('https://api.openbrewerydb.org/breweries')
print(response_API.jason())
