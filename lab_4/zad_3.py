class Property():
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, plot: int):
        self.plot = plot

    def __str__(self):
        return ""

class Flat(property):
    def __init__(self,floor):
        self.floor = floor

    def __str__(self):
        return ""