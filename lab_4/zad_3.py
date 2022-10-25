class Property():
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"{self.area} {self.rooms} {self.price} {self.address} {self.plot}"


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"{self.area} {self.rooms} {self.price} {self.address} {self.floor}"
