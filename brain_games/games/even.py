from random import randint


INFO = 'Answer "yes" if the number is even, otherwise answer "no".'
NUM_MIN = 1
NUM_MAX = 100


def even(number):
    return 'yes' if number % 2 == 0 else 'no'


def generate_round(number_min, number_max):
    number = randint(number_min, number_max)
    correct_answer = even(number)
    return number, correct_answer
