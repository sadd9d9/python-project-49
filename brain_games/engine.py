import prompt


def play(start, question_and_answer):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(start)

    for i in range(3):
        question = question_and_answer[i][0]
        correct_answer = question_and_answer[i][1]
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return

    print(f"Congratulations, {name}!")
