from dunder import Product    # Parent class

# Child class
class Drink(Product):    # Drink是Product的子孫，Product是Parent Class
    def __init__(self, name, price, volume):    # __init__會取代parent class的__init__ => overwrite
        super().__init__(name, price)           # super可以執行/呼叫parent class裡的function(即使覆寫)
        self.volume = volume

d = Drink('珍珠奶茶', 80, 600)
d.name
# print(d.name)
print(d.volume)
