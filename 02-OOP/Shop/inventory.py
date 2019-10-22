import sys
from product import Product

class Shop():
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add_to_inventory(self, it):
        if isinstance(it, Product):
            self.inventory.append(it)
        else:
            sys.stdout.write("{} is not an object of class Product.\n".format(it))
    
    def inventory_total_price(self):
        t = 0
        for p in range(len(self.inventory)):
            t += self.inventory[p].price * self.inventory[p].quantity
        
        return t