

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Mad Libs \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_noun():
    noun = input('Enter a noun: ')
    return noun


def get_verb():
    verb = input('Enter a verb: ')
    return verb


def get_adjective():
    adjective = input('Enter a adjective: ')
    return adjective

def get_adverb():
    adverb = input('Enter a adverb: ')
    return adverb

def print_mad_lib(noun, verb, adjective, adverb):
    print(f'Do you {verb} your {adjective} {noun} {adverb}? That\'s hilarious!')

if __name__ == "__main__":
    
    noun = get_noun()
    verb = get_verb()
    adjective = get_adjective()
    adverb = get_adverb()
    print_mad_lib(noun, verb, adjective, adverb)