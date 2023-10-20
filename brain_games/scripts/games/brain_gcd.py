#!/usr/bin/env python3
import prompt
import math
from random import randint
from brain_games.my_function import welcome


def my_gcd():
    welcome()
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Find the greatest common divisor of given numbers.')
    l_num = randint(0, 100)
    r_num = randint(0, 100)
    print('Question: ', str(l_num), str(r_num))
    f_num = prompt.integer('Your answer: ')
    if f_num == math.gcd(l_num, r_num):
        print('Correct!')
        print('Congratulations, ' + name + '!')
    else:
        print("'" + str(f_num) + "'" + " is wrong answer ;(. Correct answer was " + "'" + str(math.gcd(l_num, r_num)) + "'")
        print("Let's try again, " + name + "!")


if __name__ == '__main__':
    my_gcd()
