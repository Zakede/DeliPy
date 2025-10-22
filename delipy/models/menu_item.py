class MenuItem:
    def __init__(self, id: int, name: str, price: float, description: str, category: str):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.category = category

    def __str__(self):
        return f"{self.name} (${self.price}) - {self.description}: {self.category}"
