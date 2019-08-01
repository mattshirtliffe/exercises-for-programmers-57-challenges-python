
def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Parsing a data file \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_record_from_file():
    keys = ['last', 'first', 'salary']
    with open("names.csv") as file:
        for l in file.readlines():
            yield dict(zip(keys,[e.rstrip() for e in l.split(',')]))


def print_headings():
    headings = ['Last', 'First', 'Salary']
    heading = ''
    for i, h in enumerate(headings):
        if i is not len(headings)-1:
            heading += f'{h}     '
        else:
            heading += f'{h}'
    print(heading)
    print(len(heading) * '-')


def print_records():
    for record in get_record_from_file():
        for key, value in record.items():
            end_spaces = (len(key)+5) * ' '
            value += end_spaces[len(value):]
            print(value, end='')
        print()


if __name__ == "__main__":
    print_header()
    print_headings()
    print_records()