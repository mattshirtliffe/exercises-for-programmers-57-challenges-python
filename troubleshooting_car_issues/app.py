

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Troubleshooting car issues \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_yes_or_no(question):

    while True:
        answer = input(question)
        answer = answer.lower()
        if answer == 'y' or answer == 'yes':
            return True
        elif answer == 'n' or answer == 'no':
            return False
        else:
            print('A valid input is required')



def print_answer(answer):
    print(answer)


if __name__ == "__main__":
    
    print_header()
    if get_yes_or_no('Is the car silent when you turn the key? '):
        if get_yes_or_no('Are the battery terminals corroded? '):
            print('Clean terminals and try starting again')
        else:
            print('Replace cables and try again')
    else:
        if get_yes_or_no('Does the car make a clicking noise? '):
            print('Replace the battery')
        else:
            if get_yes_or_no('Does the car crank up but fail to start? '):
                print('Check spark blug connections')
            else:
                if get_yes_or_no('Does the engine start and then die? '):
                    if get_yes_or_no('Does your car have fuel injection? '):
                        print('Ge it in for service')
                    else:
                        print('Check to ensure the choke is opening and closing')
                        