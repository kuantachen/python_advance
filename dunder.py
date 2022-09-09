class Product:
    def __init__(self, name, price):
        self.name = name    # property
        self.price = price  # property

    def __str__(self):      # 會決定print什麼物件(盡量印出可讀性高的)
        # return self.name + ' ' + str(self.price)
        return f'{self.name} ${self.price}'
    
    def __repr__(self):     # representatoin顯示明確且較詳盡的資訊
        return f'<Product({self.name}, {self.price})>'

    def __add__(self, other):
        if isinstance(other, str):
            self.name += other
        if isinstance(other, Product):
            return [self, other]

    def __mul__(self, other):
        re = []
        if isinstance(other, int):
            for _ in range(other):
                re.append(self)
        return re


p1 = Product('珍珠奶茶', 60)    # instance 實例
p2 = Product('義大利麵', 120)
# p + '白玉'
# print(p1 + p2)
# print(p1 * 5)
# print(repr(p))


class ShoppingCart:
    def __init__(self, products):
        self.products = products

    def __getitem__(self, key):
        return self.products[key]

s = ShoppingCart([p1, p2])
# print(s[0])

if __name__ == '__main__':
    print(p1 * 5)
    print(s[0])