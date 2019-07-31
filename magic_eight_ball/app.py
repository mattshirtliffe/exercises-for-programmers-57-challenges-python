import random

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Magic 8 Ball \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_question():
    while True:
        question = input('What\'s your question? ')
        if len(question) > 0:
            return question
        else:
            print('A valid input is required')

def print_response():
    responses = ['Yes', 'No', 'Maybe', 'Ask again later.']
    response = random.choice(responses)
    print(response)

if __name__ == "__main__":
    print_header()
    get_question()
    print_response()