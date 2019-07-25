

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Temperature Converter \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)


def print_prompt():
    print('Press C to convert from Fahernheit to Celsius.\nPress F to convert from Celsius to Fahernheit.\n')

def get_temp_format():
    temp_formats = ['C', 'F']
    while True:
        temp_format = input('What choice: ')
        if temp_format in temp_formats:
            return temp_format
        
        print('A valid input is required')

def get_temperature(temperature_format):
    temperature_formats = {'F':'Fahernheit', 'C': 'Celsius'}

    while True:
        try:
            temperature = input(f'Please enter the temperature in {temperature_formats[temperature_format]}: ')
            return float(temperature)
        except ValueError:
            print('a valid input required')

def print_temperature(temperature_format, temperature):
    temperature_formats = {'F':'Fahernheit', 'C': 'Celsius'}
    print(f'The temperature in {temperature_formats[temperature_format]} is {temperature}')

def celsius_to_fahernheit(temperature_c):
    fahernheit = (temperature_c * 9/5) + 32
    return fahernheit

def fahernheit_to_celsius(temperature_f):
    celsius = (temperature_f-32) * 5/9
    return celsius

if __name__ == "__main__":
    print_header()
    print_prompt()
    temperature_format = get_temp_format()
    temperature = get_temperature(temperature_format)
    if temperature_format == 'C':
        temperature = fahernheit_to_celsius(temperature)
        print_temperature(temperature_format, temperature)

    if temperature_format == 'F':
        temperature = celsius_to_fahernheit(temperature)
        print_temperature(temperature_format, temperature)