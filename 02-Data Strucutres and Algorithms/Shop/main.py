import sys
from product import Product
from inventory import Shop

shop = Shop()

def walk_around_the_shop():
    sys.stdout.write("Welcome to Broseghini's Shop. We sell everything imaginable!\n")
    sys.stdout.write("="*60+"\n\n")
    left = False

    while not left:
        name = input("Product name: ")
        price = input("Product price: ")
        qty = input("Product quantity: ")
        product = Product(name, int(price), int(qty))

        shop.add_to_inventory(product)

        leaving = input("Do you wish to leave? (y/n): \n")
        if leaving == "y":
            left = True

    return shop


def display_cart(cart):
    for p in range(len(cart.inventory)):
        print("Product(s) name, price and quantity respectively in cart: \n")
        for k,v in cart.inventory[p].__dict__.items():
            print("{}: {}".format(k.capitalize(), v))
    
    total = 0
    for p in range(len(cart.inventory)):
        total += cart.inventory[p].price

    print(total)
def main():

    products_in_cart = walk_around_the_shop()

    display_cart(products_in_cart)

if __name__ == '__main__':
    main()