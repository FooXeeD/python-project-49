from random import randint, choice


INFO = 'What is the result of the expression?'


def random_generation(NUMBER_MIN, NUMBER_MAX):
    OPERATOR_ALL = ['+', '-', '*']
    number1 = randint(NUMBER_MIN, NUMBER_MAX)
    number2 = randint(NUMBER_MIN, NUMBER_MAX)
    operator = choice(OPERATOR_ALL)
    question = f'{number1} {operator} {number2}'
    correct_answer = str(eval(question))
    return question, correct_answer
