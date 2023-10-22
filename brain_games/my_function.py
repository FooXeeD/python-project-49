import prompt


def my_games(mygames):
    NUM_MIN = 1
    NUM_MAX = 100
    ROUND_COUNT = 3

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + str(name) + '!')
    print(mygames.INFO)

    for _ in range(ROUND_COUNT):
        question, correct_answer = mygames.random_generation(NUM_MIN, NUM_MAX)
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
    print('Congratulations, ' + str(name) + '!')
