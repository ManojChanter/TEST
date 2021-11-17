from order import order

class HotChocolate(order):

    counter = 0

    def __init__(self, size, is_dairy_free, customer_name):
        super().__init__(size, is_dairy_free, customer_name)
        HotChocolate.counter +=1
        self.id = HotChocolate.counter

    def __str__(self):
        return f"it's a {self.size} size hot chocolate. " \
                f"{'dairy free' if self.is_dairy_free else 'with dairy'}."\
                f" it's id is {self.id}"

    new_product = HotChocolate('L', False, "Manoj")

