from random import randint


INFO = 'Find the greatest common divisor of given numbers.'


def gcd(number1, number2):
    while number1 != 0 and number2 != 0:
        if number1 >= number2:
            number1 %= number2
        else:
            number2 %= number1
    return str(number1 or number2)


def random_generation(NUMBER_MIN, NUMBER_MAX):
    number1 = randint(NUMBER_MIN, NUMBER_MAX)
    number2 = randint(NUMBER_MIN, NUMBER_MAX)
    question = f'{number1} {number2}'
    correct_answer = gcd(number1, number2)
    return question, correct_answer
