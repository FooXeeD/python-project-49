from random import randint


INFO = 'What number is missing in the progression?'
NUM_MIN = 1
NUM_MAX = 100


def generate_round(number_min, number_max):
    STEP_MIN = 1
    STEP_MAX = 10
    ELEMENT_COUNT_MIN = 5
    ELEMENT_COUNT_MAX = 10

    number_start = randint(number_min, number_max)
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
