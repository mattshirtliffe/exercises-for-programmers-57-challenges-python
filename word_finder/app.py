
def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Word finder \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_text_from_file():
     with open("words.txt") as file:
        return file.read()


def replace_utilize(text):
    return text.replace('utilize', 'use')


def get_new_file_name():
    while True:
        product_name = input('What is the output file name? ')
        if len(product_name) > 0:
            return product_name
        else:
            print('A valid input required')


def create_output_file(name, content):
    with open(name, 'w') as f:
        f.writelines(content)


if __name__ == "__main__":
    print_header()
    text = get_text_from_file()
    text = replace_utilize(text)
    file_name = get_new_file_name()
    create_output_file(file_name, text)