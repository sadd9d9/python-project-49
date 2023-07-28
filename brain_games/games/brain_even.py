#!/usr/bin/env python3

from random import randint
from brain_games.engine import play


def main():
    start = 'Answer "yes" if the number is even, otherwise answer "no".'
    number_and_answer = []
    for _ in range(3):
        number = randint(1, 99)
        if number % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
        number_and_answer.append([number, answer])
    play(start, number_and_answer)


if __name__ == '__main__':
    main()
