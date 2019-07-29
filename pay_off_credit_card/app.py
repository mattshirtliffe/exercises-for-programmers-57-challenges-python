import math

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Months to Pay Off a Credit Card \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_balance():

    while True:
        try:
            balance = input('What is your balance? ')
            return int(balance)
        except ValueError:
            print('A valid input is required')


def get_apr():

    while True:
        try:
            apr = input('What is the APR on the card (as a percent)? ')
            return int(apr)
        except ValueError:
            print('A valid input is required')


def get_monthly_payments():

    while True:
        try:
            monthly_payment = input('What are the monthly payment you can make? ')
            return int(monthly_payment)
        except ValueError:
            print('A valid input is required')


def calculate_months_until_paid_off(balance, apr, monthly_payments):
    apr = apr/100
    apr = apr/365
    months_until_paid_off = (-1/30) * math.log(1+(balance/monthly_payments)*(1-(1+apr)**30),10)/math.log(1+apr,10)
    return math.ceil(months_until_paid_off)

def print_months_take_to_pay(months):
    print(f'It will take you {months} months to pay off this card')

if __name__ == "__main__":
    print_header()
    balance = get_balance()
    apr = get_apr()
    monthly_payments = get_monthly_payments()
    months_until_paid_off = calculate_months_until_paid_off(balance, apr, monthly_payments)
    print_months_take_to_pay(months_until_paid_off)

