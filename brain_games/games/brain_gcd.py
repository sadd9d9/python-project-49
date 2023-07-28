#!/usr/bin/env python3

from random import randint
from math import gcd
from brain_games.engine import play


def main():
    start = "Find the greatest common divisor of given numbers."
    question_and_answer = []
    for _ in range(3):
        a = randint(2, 100)
        b = randint(2, 100)
        while gcd(a, b) <= 1:
            a = randint(2, 100)
            b = randint(2, 100)
        question = str(a) + ' ' + str(b)
        answer = str(gcd(a, b))
        question_and_answer.append([question, answer])
    play(start, question_and_answer)


if __name__ == '__main__':
    main()
