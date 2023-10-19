#!/usr/bin/env python3
import prompt
from random import randint


def my_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    r_num = randint(1, 100)
    print('Question: ' + str(r_num))
    f_num = prompt.string('Your answer: ')
    if f_num == 'yes' and r_num % 2 == 0 or f_num == 'no' and r_num % 2 != 0:
        print('Correct!')
        r_num2 = randint(1, 100)
        print('Question: ' + str(r_num2))
        sec_num = prompt.string('Your answer: ')
        if sec_num == 'yes' and r_num2 % 2 == 0 or sec_num == 'no' and r_num2 % 2 != 0:
            print('Correct!')
            r_num3 = randint(1, 100)
            print('Question: ' + str(r_num3))
            th_num = prompt.string('Your answer: ')
            if th_num == 'yes' and r_num3 % 2 == 0 or th_num == 'no' and r_num3 % 2 != 0:
                print('Congratulations, ' + name + '!')
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print("Let's try again, " + name + "!")
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, " + name + "!")
    else:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        print("Let's try again, " + name + "!")


if __name__ == '__main__':
    my_even()
