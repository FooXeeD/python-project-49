from random import randint


INFO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(number):
    if number < 2:
        return 'no'
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def random_generation(NUMBER_MIN, NUMBER_MAX):
    number = randint(NUMBER_MIN, NUMBER_MAX)
    correct_answer = prime(number)
    return number, correct_answer
