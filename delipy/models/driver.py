from .user import User

class Driver(User):
    def __init__(self, id: int, name: str, email: str, password: str, vehicle_type: str, rating=0):
        super().__init__(id, name, email, password, rating)
        self.vehicle_type = vehicle_type
