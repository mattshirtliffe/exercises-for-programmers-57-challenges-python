
def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Word frequency finder \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def get_text_from_file():
     with open("words.txt") as file:
        return file.read()


def count_frequency(text):
    text_list = text.split()
    # word_frequency = []
    # for word in text_list:
    #     word_frequency.append(text_list.count(word))

    # print(text_list)
    # print(word_frequency)
    # return dict(zip(text_list,word_frequency))
    return dict(zip(text_list, [text_list.count(word) for word in text_list])) 


def print_frequency_histogram(words_freq):
    for key, value in words_freq.items():
        h = '*' * value
        print(f'{key}: {h}')
    print()


if __name__ == "__main__":
    print_header()
    text = get_text_from_file()
    word_freq = count_frequency(text)
    print_frequency_histogram(word_freq)
    