import json


def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Product search \n'
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


def get_products_from_file():
    with open("products.json") as file:
        data = json.load(file)
        return data


def get_product_from_products(product_name, products):
    # for product in products:
    #     if product['name'] == product_name:
    #         return product
    
    # return [x for x in products if x['name'] == product_name][0]
    # return list(filter(lambda product: product_name in products['name'], products))
    # return next(product for product in products if product["name"] == product_name)
    # return list(filter(lambda p: p['name'] == product_name, products))[0]
    # return next(product for product in products if product["name"] == product_name)
    # return [x for x in products if x['name'] == product_name][0] # fastests
    
    found = [x for x in products if x['name'] == product_name] # fastests
    if len(found) > 0:
        return found[0]


def print_product(product):
    name = product['name']
    price = product['price']
    quantity = product['quantity']
    print(f'Name: {name}')
    print(f'Name: {price}')
    print(f'Name: {quantity}')


if __name__ == "__main__":
    print_header()
    products = get_products_from_file()
    while True:
        product_name = get_product_name()
        product = get_product_from_products(product_name, products['products'])
        if product:
            print_product(product)
            break
        else:
            print('Sorry, that prouct was not found in our inventory.')