from .menu import Menu

class Restaurant:
    def __init__(self, restaurant_id: int, name: str, address: str, rating=0):
        self.restaurant_id = restaurant_id
        self.name = name
        self.address = address
        self.rating = rating
        self.menu = Menu()

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = max(0, min(value, 5))
