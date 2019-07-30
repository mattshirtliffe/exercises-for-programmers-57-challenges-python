

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Multiplication table \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def multiply(a, b):
    return a * b

def create_table_list():
    cols = 13
    rows = 13
    for row in range(rows):
        if row == 0:
            print('*', end='|')
            for i in range(13):
                print(i, end='|')
            print('')    
        else:
            print('')
        for col in range(cols):
            if col == 0:
                print(row, end='|')
            print(col * row, end='|')
            

def print_output():
    output = ""
    for i in range(13):
        for j in range(13):
            output += f'{i} X {j} = {j*i}\n'
    print(output)




if __name__ == "__main__":
    
    print_header()
    create_table_list()
    print()
    print_output()
