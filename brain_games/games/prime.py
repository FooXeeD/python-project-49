from random import randint


INFO = 'Answer "yes" if given number is prime. Otherwise answer "no".'
NUM_MIN = 1
NUM_MAX = 100
ROUND_COUNT = 3


def prime(number):
    if number < 2:
        return 'no'
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def generate_round():
    number = randint(NUM_MIN, NUM_MIN)
    correct_answer = prime(number)
    return number, correct_answer
