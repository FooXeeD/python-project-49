from random import randint


INFO = 'Answer "yes" if the number is even, otherwise answer "no".'
NUM_MIN = 1
NUM_MAX = 100


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = randint(NUM_MIN, NUM_MAX)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
