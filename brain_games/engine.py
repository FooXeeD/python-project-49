import prompt


def games(games):
    ROUND_COUNT = 3

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + str(name) + '!')
    print(games.INFO)

    for _ in range(ROUND_COUNT):
        question, answer = games.generate_round(games.NUM_MIN, games.NUM_MAX)
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            return
    print('Congratulations, ' + str(name) + '!')
