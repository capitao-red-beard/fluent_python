from collections import namedtuple


# Function oriented strategy.
Customer = namedtuple('Customer', 'name fidelity')


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
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            # To compute discount call the self.promotion function.
            discount = self.promotion(self)
        return self.total() - discount


# No abstract class.
# Each strategy is a function.
def fidelity_promo(order):
    """ 5% discount for customers with 1000 or more fidelity points."""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_promo(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

# 2 customers joe has 0 points, ann has 1100
joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
# One shopping cart with 3 line items.
cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]
# FidelityPromo gives no discount to Joe as he has no points.
print(Order(joe, cart, fidelity_promo))
# Ann gets a 5% discount because she has > 1000 points.
print(Order(ann, cart, fidelity_promo))
# Banana cart has 30 banana units and 10 apple.
banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]
# Joe gets $1.50 discount thanks to BulkItemPromo.
print(Order(joe, banana_cart, bulk_item_promo))
# long_order has 10 different items as $1.00 each.
long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
# Joe gets a 7% discount on the whole order because of LargeOrderPromo.
print(Order(joe, long_order, large_order_promo))
print(Order(ann, cart, large_order_promo))