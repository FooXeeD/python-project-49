import prompt


def run_game(game):
    ROUND_COUNT = 3

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + str(name) + '!')
    print(game.INFO)

    for _ in range(ROUND_COUNT):
        question, answer = game.generate_round()
        print('Question: ' + str(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{answer}'")
            print(f"Let's try again, {name}!")
            return
    print('Congratulations, ' + str(name) + '!')
