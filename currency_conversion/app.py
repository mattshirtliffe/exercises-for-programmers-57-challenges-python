

def print_header(text):
    """ Print header 
    """
    header_text = ''
    TEXT = f' {text} \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)

def get_euros_exchanging():
    euros = input(f'How may euros are you exchanging?: ')
    while True:
        try:
            euros = float(euros)
            return euros
        except ValueError:
            print('A valid input required')


def get_exchange_rate():
    exchange_rate = input('What is the exchange rate?: ')
    while True:
        try:
            return float(exchange_rate)
        except ValueError:
            print('A valid input required')


def print_rate(euros, rate):
    print(f'{euros} euros at exchange rage of {rate}')


def print_dollars(dollars):
    print(f'{dollars} US dollars')


def calculate_amount(euro, exchange_rate):
    return round(float(euro) * (exchange_rate/100), 2)
