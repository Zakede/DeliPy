from delipy.models.menu_item import MenuItem
from delipy.models.restaurant import Restaurant

# Restaurants
pizza_place = Restaurant(1, "Pizzazz", "69 Bingus St")
burger_joint = Restaurant(2, "BurgerBooz", "BooBoo Side Rd")

# Menu items
margherita = MenuItem(1, "Margherita Pizza", 8.99, "Classic pizza with cheese and tomato", "Italian")
pepperoni = MenuItem(2, "Pepperoni Pizza", 10.99, "Spicy pepperoni pizza", "Italian")
cheeseburger = MenuItem(3, "Cheeseburger", 5.99, "Juicy burger with cheese", "Fast Food")

# Add to menus
pizza_place.menu.add_item(margherita)
pizza_place.menu.add_item(pepperoni)
burger_joint.menu.add_item(cheeseburger)

# Print menus
print(pizza_place.menu)