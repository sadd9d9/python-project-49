#!/usr/bin/env python3

from random import randint
from brain_games.engine import play


def main():
    start = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question_and_answer = []
    for _ in range(3):
        number = randint(2, 23)
        answer = 'yes'
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                answer = 'no'
        question_and_answer.append([number, answer])
    play(start, question_and_answer)


if __name__ == '__main__':
    main()
