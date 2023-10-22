from random import randint


INFO = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(number):
    return 'yes' if number % 2 == 0 else 'no'


def random_generation(NUMBER_MIN, NUMBER_MAX):
    number = randint(NUMBER_MIN, NUMBER_MAX)
    correct_answer = even(number)
    return number, correct_answer
