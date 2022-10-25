from zad_1 import Student
from zad_2 import Library, Employee, Book, Order
from zad_3 import Flat, House

# Zadanie 1

Student1 = Student("Adam", [55, 43, 60, 50, 75])
Student2 = Student("Adam", [3, 3, 5, 4, 2])

print(Student1.is_passed())
print(Student2.is_passed())

# Zadanie 2

Biblioteka1 = Library("Katowice", "Wyborcza 2a", "44-244", "8-20", "759305723")
Biblioteka2 = Library("Gliwice", "Janowska 45b", "44-786", "7-18", "374910364")

Książka1 = Book(Biblioteka1, "24/05/2012", "Adam", "Mickiewicz", 235)
Książka2 = Book(Biblioteka2, "23/04/2012", "Jan", "Mickiewicz", 245)
Książka3 = Book(Biblioteka2, "22/03/2012", "Adam", "Tkacz", 235)
Książka4 = Book(Biblioteka1, "21/02/2012", "Tomasz", "Mickiewicz", 135)
Książka5 = Book(Biblioteka2, "20/01/2012", "Adam", "Wacz", 735)

Pracownik1 = Employee("Test", "Test", "Test", "Test", "Test", "Test", "Test", "Test")
Pracownik2 = Employee("Tomasz", "Adamczyk", "24/07/2020", "28/01/1998", "Katowice", "Adamska 34c", "44-253",
                      "485940374")
Pracownik3 = Employee("Jan", "Tomaczyk", "20/07/2020", "20/01/1997", "Gliwice", "Jamska 28c", "44-273", "3859403856")

Student3 = Student("Adam", [5, 5, 5, 5, 5, 5])
Student4 = Student("Jan", [4, 4, 4, 3, 2])
Student5 = Student("Tomasz", [4, 4, 4])

Order1 = Order(Pracownik2, Student4, [Książka1, Książka2, Książka3], "20/03/2022")
Order2 = Order(Pracownik3, Student5, [Książka5, Książka4], "10/07/2021")

print(Order1)
print(Order2)

# Zad 3

Flat1 = Flat("test")
