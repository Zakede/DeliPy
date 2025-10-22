from delipy.models.user import User
from delipy.models.restaurant import Restaurant


def main():
    user = User(1, "Zake", "Tokyo")
    restraunt = Restaurant(69, "bongus", "20th av", 5)
    print(restraunt)

if __name__ == "__main__":
    main()
