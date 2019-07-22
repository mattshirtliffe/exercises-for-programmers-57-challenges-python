
def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Self-Checkout \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_item_price(item_number):
    while True:
        try:
            item_price = input(f'Enter the price of item {item_number}: ')
            return int(item_price)
        except ValueError:
            print('A valid input required')


def get_item_quantity(item_number):
    while True:
        try:
            item_price = input(f'Enter the quantity of item {item_number}: ')
            return int(item_price)
        except ValueError:
            print('A valid input required')


def get_items_subtotal(item_prices):
    return sum(item_prices)


def get_price_of_items(price, quantity):
    return price * quantity


def get_tax(subtotal, tax_rate=5.5):
    tax = (subtotal * tax_rate) / 100
    return tax


def get_total(subtotal, tax):
    return subtotal + tax


def print_subtotal(subtotal):
    print(f'Subtotal: {subtotal}')


def print_tax(tax):
    print(f'Tax: {tax}')


def print_total(total):
    print(f'Total: {total}')

if __name__ == "__main__":
    print_header()
    item_prices = []
    for i in range(3):
        i += 1
        price = get_item_price(i)
        quantity = get_item_quantity(i)
        price_of_items = get_price_of_items(price, quantity)
        item_prices.append(price_of_items)
    subtotal = get_items_subtotal(item_prices)
    tax = get_tax(subtotal)
    total = get_total(subtotal, tax)
    print_subtotal(subtotal)
    print_tax(tax)
    print_total(total)
