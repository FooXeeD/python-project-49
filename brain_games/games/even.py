from random import randint


INFO = 'Answer "yes" if the number is even, otherwise answer "no".'
NUM_MIN = 1
NUM_MAX = 100
ROUND_COUNT = 3


def even(number):
    return 'yes' if number % 2 == 0 else 'no'


def generate_round():
    number = randint(NUM_MIN, NUM_MAX)
    correct_answer = even(number)
    return number, correct_answer
