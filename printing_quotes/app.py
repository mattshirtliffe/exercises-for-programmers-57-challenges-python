

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Printing Quotes \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_quote():
    quote = input('What is the quote? ')
    return quote


def get_author_name():
    author = input('Who said it? ')
    return author


def print_quotes(author_name, quote):
    """ Print quotes
    """
    print(f'{author_name} says, \"{quote}\"')


if __name__ == "__main__":
    quote = get_quote()
    author_name = get_author_name()
    print_quotes(author_name, quote)
    