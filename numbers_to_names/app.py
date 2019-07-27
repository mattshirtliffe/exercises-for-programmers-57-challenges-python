

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Numbers to Names \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_month_number():
    
    ERROR_MESSAGE = 'A valid month number is required'
    
    while True:
        try:
            month_number = input('Please enter the number of the month?: ')
            month_number = int(month_number)
            if month_number >= 1 and month_number <= 12:
                return month_number
            else:
                print(ERROR_MESSAGE)
        except ValueError:
            print(ERROR_MESSAGE)


def get_month_from_number(month_number):

    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    # months = [
    #     "January",
    #     "February",
    #     "March",
    #     "April",
    #     "May",
    #     "June",
    #     "July",
    #     "August",
    #     "September",
    #     "October",
    #     "November",
    #     "December"
    # ]

    # months[month_number -1]

    return months.get(month_number, 'invalid month number')

    
def print_name_of_month_message(month):
    print(f'The name of the month is {month}')


if __name__ == "__main__":
    print_header()
    month_number = get_month_number()
    month = get_month_from_number(month_number)
    print_name_of_month_message(month)