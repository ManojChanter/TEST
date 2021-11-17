from order import Order
from kitchen import Kitchen
from hot_chocolate import HotChocolate


class Store:

    def __init__(self, cash):
        self.balance = cash
        self.incoming_orders = []
        self.outgoing_products = []

    def get_new_order(self, size, is_dairy_free, customer_name, price):
        self.incoming_orders.append(Order(size, is_dairy_free, customer_name))
        self.balance += price

    def forward_orders(self, kitchen):
        kitchen.receive_orders(self.incoming_orders)
        self.incoming_orders = []

    def receive_products(self, products):
        self.outgoing_products.extend(products)

    def serve_customer(self, customer_name):
        try:
            product = next(item for item in self.outgoing_products if item.customer == customer_name)
            print(f"Hey {customer_name}, your {product.size} sized hot chocolate is here!")
            self.outgoing_products.remove(product)
        except StopIteration:
            print(f"Sorry, {customer_name} we don't have your order.")