from order import Order


class HotChocolate(Order):

    counter = 0

    def __init__(self, size, is_dairy_free, customer_name):
        super().__init__(size, is_dairy_free, customer_name)
        HotChocolate.counter += 1
        self.id = HotChocolate.counter

    def __str__(self):
        return f"It's a {self.size} size hot chocolate. " \
               f"{'Dairy free' if self.is_dairy_free else 'With dairy'}. " \
               f"It's id is {self.id}."


new_product = HotChocolate('L', False, 'Sara')
print(new_product)

new_product2 = HotChocolate('L', True, 'Kate')
print(new_product2)