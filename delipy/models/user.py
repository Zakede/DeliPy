import re


class User:
    def __init__(self, id: int, name: str, email: str, password: str, rating=0):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = max(0, min(value, 5))

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if User.is_valid_email(value): 
            self._email = value
        else:
            raise ValueError(f"Invalid email: {value}")

    @staticmethod
    def is_valid_email(email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.match(pattern, email))