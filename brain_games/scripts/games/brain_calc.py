#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.my_function import welcome


def my_calc():
    welcome()
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What is the result of the expression?')
    l_num = randint(1, 100)
    r_num = randint(1, 100)
    print('Question: ' + str(l_num) + '+' + str(r_num))
    f_num = prompt.integer('Your answer: ')
    if f_num == l_num + r_num:
        print('Correct!')
        l_num2 = randint(1, 100)
        r_num2 = randint(1, 100)
        print('Question: ' + str(l_num2) + '-' + str(r_num2))
        sec_num = prompt.integer('Your answer: ')
        if sec_num == l_num2 - r_num2:
            print('Correct!')
            l_num3 = randint(1, 100)
            r_num3 = randint(1, 100)
            print('Question: ' + str(l_num3) + '*' + str(r_num3))
            th_num = prompt.integer('Your answer: ')
            if th_num == l_num3 * r_num3:
                print('Correct!')
                print('Congratulations, ' + name + '!')
            else:
                print("'" + str(th_num) + "'" + " is wrong answer ;(. Correct answer was " + "'" + str(l_num3 * r_num3) + "'")
                print("Let's try again, " + name + "!")
        else:
            print("'" + str(sec_num) + "'" + " is wrong answer ;(. Correct answer was " + "'" + str(l_num2 - r_num2) + "'")
            print("Let's try again, " + name + "!")
    else:
        print("'" + str(f_num) + "'" + " is wrong answer ;(. Correct answer was " + "'" + str(l_num + r_num) + "'")
        print("Let's try again, " + name + "!")


if __name__ == '__main__':
    my_calc()
