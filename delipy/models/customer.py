from .user import User

class Customer(User):
    def __init__(self, id: int, name: str, email: str, password: str, address: str, rating=0):
        super().__init__(id, name, email, password, rating)
        self.address = address
