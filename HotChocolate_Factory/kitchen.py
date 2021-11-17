from order import Order
from hot_chocolate import HotChocolate


class Kitchen:

    def __init__(self, staff_size, milk=50):
        self.staff_size = staff_size
        self.orders = []
        self.products = []
        self.milk = milk

    def receive_orders(self, new_orders):
        self.orders.extend(new_orders)

    @staticmethod
    def get_milk_amount(size):
        match size:
            case 'S':
                return 3
            case 'M':
                return 4
            case 'L':
                return 5
            case _:
                return 0            #we don't know the size so we provide a fallback

    def process_orders(self):
        if self.staff_size <= 0:
            raise ValueError("Soorrrryy! The kitchen can't operate without staff.")

        for order in self.orders:
            if isinstance(order, Order):
                self.make_hot_chocolate(order)
            else:
                print("Sorry we can't process this order.")

        self.orders = []

    def forward_products(self, store):
        store.receive_products(self.products)
        self.products = []

    def make_hot_chocolate(self, order):

        if order.is_dairy_free:
            self.products.append(HotChocolate(order.size, order.is_dairy_free, order.customer))
        else:
            milk_amount = self.get_milk_amount(order.size)
            if self.milk < milk_amount:
                print(f"Sorry, {order.customer} but we ran out of milk.")
            else:
                self.milk -= milk_amount
                self.products.append(HotChocolate(order.size, order.is_dairy_free, order.customer))