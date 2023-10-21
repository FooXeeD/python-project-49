import prompt


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    return name


def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    else:
        return True
