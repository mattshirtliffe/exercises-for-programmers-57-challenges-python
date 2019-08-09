import json
import os
import random

def print_header():
    """ Print header 
    """
    header_text = ''
    TEXT = f' Trivia App \n'
    line = '-' * len(TEXT)
    line += '\n'

    header_text += line
    header_text += TEXT
    header_text += line
    print(header_text)

def read_questions_from_file():
    file_name = 'questions.json'
    if os.path.exists(file_name):
        with open(file_name) as f:
            try:
                data = json.load(f)
                return data
            except:
                return {}
    else:
        print('error')


def select_random_question(data):
    questions = data['questions']
    return random.choice(questions)


def print_question(question):
    print(question['question'])


def print_answers(question):
    for index, answer in enumerate(question['answers']):
        a = answer['answer']
        print(f'{index+1}: {a}')


def get_answer(number_of_answers):
    while True:
        try:
            answer_number = input('Answer number: ')
            answer_number = int(answer_number)
            if answer_number <= number_of_answers:
                return answer_number
            else:
                print('A valid input required')    
        except ValueError:
            print('A valid input required')


def check_answer(answer_number, answers):
    answer_number -= 1
    return answers[answer_number]['is_correct']


if __name__ == "__main__":
    number_of_correct = 0
    print_header()
    data = read_questions_from_file()
    while True:
        question = select_random_question(data)
        
        print_question(question)
        print_answers(question)
        answer_number = get_answer(len(question['answers']))

        is_correct = check_answer(answer_number,question['answers'])
        if is_correct:
            number_of_correct += 1
        else:
            break
    

    print(f'Number of correct answers: {number_of_correct}')