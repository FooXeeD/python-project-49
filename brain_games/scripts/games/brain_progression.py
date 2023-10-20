#!/usr/bin/env python3
import prompt
from brain_games.my_function import welcome


def my_progression():
    welcome()
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('What number is missing in the progression?')
    lst = [i for i in range(0, 20, 2)]
    my_string = " ".join(str(element) for element in lst)
    new_text = my_string[:10] + ".." + my_string[12:]
    print('Question: ', str(new_text))
    first_num = prompt.integer('Your answer: ')
    if lst[5] == first_num:
        print('Correct!')
        lst2 = [i for i in range(20, 40, 2)]
        my_string2 = " ".join(str(element) for element in lst2)
        new_text2 = my_string2[:6] + ".." + my_string2[8:]
        print('Question: ', str(new_text2))
        second_num = prompt.integer('Your answer: ')
        if lst2[2] == second_num:
            print('Correct!')
            lst3 = [i for i in range(60, 80, 2)]
            my_string3 = " ".join(str(element) for element in lst3)
            new_text3 = my_string3[:24] + ".." + my_string3[26:]
            print('Question: ', str(new_text3))
            third_num = prompt.integer('Your answer: ')
            if lst3[8] == third_num:
                print('Correct!')
                print('Congratulations, ' + name + '!')
            else:
                print("'" + str(third_num) + "'" + " is wrong answer ;(. Correct answer was " + "'" + str(lst3[8]) + "'")
                print("Let's try again, " + name + "!")
        else:
            print("'" + str(second_num) + "'" + " is wrong answer ;(. Correct answer was " + "'" + str(lst2[2]) + "'")
            print("Let's try again, " + name + "!")
    else:
        print("'" + str(first_num) + "'" + " is wrong answer ;(. Correct answer was " + "'" + str(lst[5]) + "'")
        print("Let's try again, " + name + "!")


if __name__ == '__main__':
    my_progression()
