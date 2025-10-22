from .menu_item import MenuItem

class Menu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, item):
        self.menu_items.append(item)

    def remove_item(self, item):
        if item in self.menu_items:
            self.menu_items.remove(item)

    def get_menu(self):
        return self.menu_items

    def __str__(self):
        if not self.menu_items:
            return "Menu is empty."
        # Use each item's __str__
        return "\n".join(str(item) for item in self.menu_items)
