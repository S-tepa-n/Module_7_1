class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return (f'{self.name},{self.weight},{self.category}')


class Shop:
    __file_name = 'products.txt'
    file = open(__file_name, 'w')
    file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        p_file = file.read()
        file.close()
        return p_file

    def add(self, *product):
        for i in product:
            _products = self.get_products()
            if i.name in _products:
                print(f'Продукт {i.name} уже есть в магазине!')
            else:
                _file = open(self.__file_name, 'a')
                _file.write(f'{i}\n')
                _file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
