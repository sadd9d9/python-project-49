#!/usr/bin/env python3

from random import randint
from brain_games.engine import play


def main():
    start = "What is the result of the expression?"
    operations = {0: '+', 1: '-', 2: '*'}
    question_and_answer = []
    for _ in range(3):
        number1 = randint(1, 20)
        number2 = randint(1, 20)
        operation = randint(0, 2)
        question = f"{number1} {operations[operation]} {number2}"
        answer = str(eval(question))
        question_and_answer.append([question, answer])
    play(start, question_and_answer)


if __name__ == '__main__':
    main()
