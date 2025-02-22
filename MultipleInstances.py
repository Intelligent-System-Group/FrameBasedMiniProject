class Entree:
    def __init__(self, entree_name, type):
        self.entree_name = entree_name
        self.type = type

class Beverage:
    def __init__(self, beverage_name, size):
        self.beverage_name = beverage_name
        self.size = size

class Dessert:
    def __init__(self, dessert_name, flavor):
        self.dessert_name = dessert_name
        self.flavor = flavor

class MyOrder(Entree, Beverage, Dessert):
    def __init__(self, entree_name, type, beverage_name, size,
                 dessert_name, flavor, total_price):
        
        Entree.__init__(self, entree_name, type)
        Beverage.__init__(self, beverage_name, size)
        Dessert.__init__(self, dessert_name, flavor)
        
        self.total_price = total_price

    def display_info(self):
        print("I would like to order:")
        print(f"Main Dish: {self.entree_name} ({self.type})")
        print(f"Beverage: {self.beverage_name} ({self.size})")
        print(f"Dessert: {self.dessert_name} ({self.flavor})")
        print(f"Price: ${self.total_price:.2f}")

Order = MyOrder(
    entree_name="Beef Wellington",
    type="Meat",
    beverage_name="Cola",
    size="Large",  
    dessert_name="Sticky Toffee Pudding",
    flavor="Caramel",
    total_price=365.12  
)

Order.display_info()
