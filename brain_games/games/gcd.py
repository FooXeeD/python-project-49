from random import randint


INFO = 'Find the greatest common divisor of given numbers.'
NUM_MIN = 1
NUM_MAX = 100


def gcd(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 >= number2:
            number1 %= number2
        else:
            number2 %= number1
    return str(number1 or number2)


def generate_round(number_min, number_max):
    number1 = randint(number_min, number_max)
    number2 = randint(number_min, number_max)
    question = f'{number1} {number2}'
    correct_answer = gcd(number1, number2)
    return question, correct_answer
