from collections import namedtuple
from inspect import getmembers, isfunction


# Function oriented strategy.
Customer = namedtuple("Customer", "name fidelity")


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            # To compute discount call the self.promotion function.
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order total: {:.2f} due {:.2f}>"
        return fmt.format(self.total(), self.due())


# No abstract class.
# Each strategy is a function.
def fidelity_promo(order):
    """ 5% discount for customers with 1000 or more fidelity points."""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def large_order_promo(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


# 2 customers joe has 0 points, ann has 1100
joe = Customer("John Doe", 0)
ann = Customer("Ann Smith", 1100)
# One shopping cart with 3 line items.
cart = [
    LineItem("banana", 4, 0.5),
    LineItem("apple", 10, 1.5),
    LineItem("watermellon", 5, 5.0),
]
# FidelityPromo gives no discount to Joe as he has no points.
print(Order(joe, cart, fidelity_promo))
# Ann gets a 5% discount because she has > 1000 points.
print(Order(ann, cart, fidelity_promo))
# Banana cart has 30 banana units and 10 apple.
banana_cart = [LineItem("banana", 30, 0.5), LineItem("apple", 10, 1.5)]
# Joe gets $1.50 discount thanks to BulkItemPromo.
print(Order(joe, banana_cart, bulk_item_promo))
# long_order has 10 different items as $1.00 each.
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
# Joe gets a 7% discount on the whole order because of LargeOrderPromo.
print(Order(joe, long_order, large_order_promo))
print(Order(ann, cart, large_order_promo))

# Finding strategies in a module.
promos = [
    globals()[name]
    for name in globals()
    if name.endswith("_promo") and name != "best_promo"
]


def best_promo(order):
    """Select the best discount available"""
    return max(promo(order) for promo in promos)


print(Order(joe, long_order, best_promo))
print(Order(joe, banana_cart, best_promo))
print(Order(ann, cart, best_promo))

# Command.
class MacroCommand:
    """A command that executes a list of commands"""

    # Building a list from the commands argument ensures that it is
    # iterable and keeps a local copy of the command references in each
    # MacroCommand instance.
    def __init__(self, commands):
        self.commands = list(commands)

    # When an instance of MacroCommand is invoked, each command in
    # self.commands is called in sequence.
    def __call__(self):
        for command in self.commands:
            command()
