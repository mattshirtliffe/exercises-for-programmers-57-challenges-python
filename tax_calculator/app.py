
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


def print_subtotal():
    print('')