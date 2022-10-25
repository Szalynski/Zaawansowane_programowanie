class Library():
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka znajduje się na ulicy {self.street} {self.zip_code} ' \
               f'{self.city}. Godziny otwarcia {self.open_hours}. Kontakt {self.phone}.'


class Employee():
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'{self.first_name} {self.last_name}, urodzony {self.birth_date} ' \
               f'zatrudniony {self.hire_date}. Adress {self.city} {self.zip_code} {self.street}. Kontakt {self.phone}'


class Book():
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Książka z biblioteki {self.library}. Autorstwa ' \
               f'{self.author_name} {self.author_surname} wydana ' \
               f'{self.publication_date}. Ilość stron {self.number_of_pages}'


class Order():
    def __init__(self, employee, student, books: list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Książki {self.books} zamówione przez ' \
               f'{self.student}. Data zamówienia {self.order_date}, realizator {self.employee}'
