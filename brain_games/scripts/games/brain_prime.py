#!/usr/bin/env python3
import prompt
from random import randint
from brain_games.my_function import welcome
from brain_games.my_function import check_prime


def my_prime():
    name = str(welcome())
    print('Hello, ' + name + '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    r_num = randint(1, 100)
    number_prime = check_prime(r_num)
    print('Question: ' + str(r_num) + '(' + str(number_prime) + ')')
    f_num = prompt.string('Your answer: ')
    if f_num == 'yes' and number_prime is True or f_num == 'no' and number_prime is False:
        print('Correct!')
        r_num2 = randint(1, 100)
        number_prime2 = check_prime(r_num2)
        print('Question: ' + str(r_num2) + '(' + str(number_prime2) + ')')
        f_num2 = prompt.string('Your answer: ')
        if f_num2 == 'yes' and number_prime2 is True or f_num2 == 'no' and number_prime2 is False:
            print('Correct!')
            r_num3 = randint(1, 100)
            number_prime3 = check_prime(r_num3)
            print('Question: ' + str(r_num3) + '(' + str(number_prime3) + ')')
            f_num3 = prompt.string('Your answer: ')
            if f_num3 == 'yes' and number_prime3 is True or f_num3 == 'no' and number_prime3 is False:
                print('Correct!')
                print('Congratulations, ' + name + '!')
            else:
                print("'" + str(f_num3) + "' is wrong answer ;(. Correct answer was 'no'.")
                print("Let's try again, " + name + "!")
        else:
            print("'" + str(f_num2) + "' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, " + name + "!")
    else:
        print("'" + str(f_num) + "' is wrong answer ;(. Correct answer was 'no'.")
        print("Let's try again, " + name + "!")


if __name__ == '__main__':
    my_prime()
