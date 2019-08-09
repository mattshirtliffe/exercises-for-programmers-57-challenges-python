import json
import os
from terminaltables import AsciiTable

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Tracking inventory \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_product_name():
    while True:
        product_name = input('What is the product name? ')
        if len(product_name) > 0:
            return product_name
        else:
            print('A valid input required')


def get_serial_number():
    while True:
        product_name = input('What is the serial number? ')
        if len(product_name) > 0:
            return product_name
        else:
            print('A valid input required')


def get_product_value():
    while True:
        try:
            product_value = input('What is the product value? ')
            return float(product_value)
        except ValueError:
            print('A valid input required')


def get_json_from_file():
    file_name = 'products.json'
    if os.path.exists(file_name):
        with open(file_name) as f:
            try:
                data = json.load(f)
                return data
            except:
                return {}
    else:
        return {}          


def save_product(data, product):
    with open('products.json', 'w') as f:

        products = data.get('products', None)
        if products:
            products.append(product)
            data['products'] = products
        else:
            data = {}
            data['products'] = []
            data['products'].append(product)

        f.write(json.dumps(data))
    
    return data


def print_products(data):
    products = data['products']
    headings = products[0].keys()
    table_data = [
        headings
    ]

    for product in products:
        d = []
        for i,v in product.items():
            d.append(v)
        table_data.append(d)

    table = AsciiTable(table_data)
    print(table.table)

if __name__ == "__main__":
    print_header()
    
    data = get_json_from_file()

    product_name = get_product_name()
    serial_number = get_serial_number()
    product_value = get_product_value()
    product = {
        'name': product_name,
        'value': product_value,
        'serial_number':serial_number
    }
    data = save_product(data, product)
    print_products(data)