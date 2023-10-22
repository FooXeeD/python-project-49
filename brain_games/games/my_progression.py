from random import randint


INFO = 'What number is missing in the progression?'


def random_generation(NUMBER_MIN, NUMBER_MAX):
    STEP_MIN = 1
    STEP_MAX = 10
    ELEMENT_COUNT_MIN = 5
    ELEMENT_COUNT_MAX = 10

    number_start = randint(NUMBER_MIN, NUMBER_MAX)
    step = randint(STEP_MIN, STEP_MAX)
    elements = randint(ELEMENT_COUNT_MIN, ELEMENT_COUNT_MAX)
    element_list = []
    for _ in range(elements):
        number_start += step
        element_list.append(str(number_start))
    missing_index = randint(0, elements - 1)
    correct_answer = str(element_list[missing_index])
    element_list[missing_index] = '..'
    question = ' '.join(element_list)
    return question, correct_answer
