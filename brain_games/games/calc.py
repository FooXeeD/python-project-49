from random import randint, choice


INFO = 'What is the result of the expression?'
NUM_MIN = 1
NUM_MAX = 100


def generate_round(number_min, number_max):
    OPERATOR_ALL = ['+', '-', '*']
    number1 = randint(number_min, number_max)
    number2 = randint(number_min, number_max)
    operator = choice(OPERATOR_ALL)
    question = f'{number1} {operator} {number2}'
    correct_answer = str(eval(question))
    return question, correct_answer