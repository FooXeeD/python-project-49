import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + str(name) + '!')
    print(game.INFO)

    for _ in range(game.ROUND_COUNT):
        question, correct_answer = game.generate_round()
        print('Question: ' + str(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
    print('Congratulations, ' + str(name) + '!')
