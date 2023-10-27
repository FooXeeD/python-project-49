from random import randint, choice


INFO = 'What is the result of the expression?'
NUM_MIN = 1
NUM_MAX = 100
ROUND_COUNT = 3
OPERATOR_ALL = ['+', '-', '*']


def generate_round():
    number1 = randint(NUM_MIN, NUM_MAX)
    number2 = randint(NUM_MIN, NUM_MAX)
    operator = choice(OPERATOR_ALL)
    question = f'{number1} {operator} {number2}'
    correct_answer = str(eval(question))
    return question, correct_answer
