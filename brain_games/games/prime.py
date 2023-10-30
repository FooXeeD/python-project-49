from random import randint


INFO = 'Answer "yes" if given number is prime. Otherwise answer "no".'
NUM_MIN = 1
NUM_MAX = 100


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def generate_round():
    number = randint(NUM_MIN, NUM_MAX)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
