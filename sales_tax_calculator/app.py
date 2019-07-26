

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Multistate sales_tax_calculator \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_order_amount():

    while True:
        try:
            weight = input('What is the order amount?: ')
            return float(weight)
        except ValueError:
            print('A valid input is required')


def get_state():

    # Sortest state names Ohio, Iowa and Utah
    while True:
        state = input('What state do you live in? ')
        if len(state) >= 4:
            return state
        else:
            print('A valid input is required')


def get_county():

    while True:
        county = input('What county do you live in? ')
        if len(county) >= 4:
            return county
        else:
            print('A valid input is required')


def calculate_state_tax(amount, state):
    state_taxes = {'Wisconsin': 5.0, 'Illinois': 8.0}
    tax = (amount * state_taxes.get(state, 0)) / 100
    return tax


def calculate_county_tax(amount, county):
    county_taxes = {'Eau Claire': 0.005, 'Dunn': 0.004}
    tax = (amount * county_taxes.get(county, 0)) / 100
    return tax

def calculate_total(amount, tax):
    return round(amount + tax, 2)
    
def print_tax(tax):
    print(f'The tax is {tax:.2f}')


def print_total(total):
    print(f'The total is {total:.2f}')


if __name__ == "__main__":
    print_header()
    amount = get_order_amount()
    state = get_state()
    tax = calculate_state_tax(amount, state)

    if state == 'Wisconsin':
        county = get_county()
        tax += calculate_county_tax(amount, county)

    if tax > 0:
        print_tax(tax)
        total = calculate_total(amount, tax)
    else:
        total = amount
    
    print_total(total)
