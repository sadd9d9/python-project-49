#!/usr/bin/env python3

from random import randint
from brain_games.engine import play


def main():
    start = "What number is missing in the progression?"
    question_and_answer = []
    for _ in range(3):
        number = randint(1, 20)
        step = randint(1, 10)
        missing_step = randint(0, 9)
        question = ''
        for i in range(10):
            if i == missing_step:
                question += '.. '
                answer = str(number)
            else:
                question += str(number) + ' '
            number += step
        question_and_answer.append([question, answer])
    play(start, question_and_answer)


if __name__ == '__main__':
    main()
