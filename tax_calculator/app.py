
def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Tax calculator \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_order_amount():
    while True:
        try:
            order_amount = input('What is the order amount? ')
            return float(order_amount)
        except ValueError:
            print('A valid input is required')

def get_state():
    states = ['WI', 'MN']
    while True:
        state = input('What is the state? ')
        if state in states:
            return state
        
        print('A valid input is required')


def print_subtotal(subtotal):
    print(f'The subtotal is {subtotal:.2f}.')


def print_total(total):
    print(f'The total is {total:.2f}.')


def print_tax(tax):
    print(f'The tax is {tax:.2f}.')


def calculate_tax(subtotal, tax_rate=5.5):
    tax = (subtotal * tax_rate) / 100
    return tax


def calculate_total(subtotal, tax):
    return subtotal + tax


def print_message(state, order_amount):
    tax = None
    if state == 'WI':
        print_subtotal(order_amount)
        tax = calculate_tax(order_amount)
        print_tax(tax)
        total = calculate_total(order_amount, tax)
        print_total(total)
    else:
        print_total(order_amount)

if __name__ == "__main__":
    print_message('WI', 10.00)
    print_message('MN', 10.00)

