# Hot Chocolate Factory
# - given a store, where the customers can submit their orders and also pay
# - the order is being forwarded to the kitchen
# - given a kitchen where the product is made.
#       In the kitchen all the resources are given (milk, cocoa , sugar) but the amount of milk is limited daily,
#       since the owner only has 5 cows.
#       Recepies: S : 3 milk, 2 cocoa, 1 sugar
#                 M : 4 milk, 3 cocoa, 2 sugar
#                 L : 5 milk, 4 cocoa, 3 sugar
# - the product can vary in size (S, M, L) and can be ordered dairy-free, with vegetable milk.
# - once the order is ready, the customer can pick it up in the store's serving window

from kitchen import Kitchen
from store import Store

my_store = Store(200)
my_store.get_new_order('S', True, 'Kate', 2)
my_store.get_new_order('L', False, 'Bob', 4)
my_store.get_new_order('L', False, 'Mary', 4)

my_kitchen = Kitchen(2, 6)
my_kitchen.receive_orders(my_store.incoming_orders)
my_kitchen.process_orders()
my_kitchen.forward_products(my_store)
my_store.serve_customer('Kate')
my_store.serve_customer('Bob')
my_store.serve_customer('Mary')
my_store.serve_customer('Kate')