#!/usr/bin/env python3

import prompt, random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    k = 0
    for _ in range(3):
        number = random.randint(1, 99)
        print(f"Question: {number}")
        answer = prompt.string("Your answer: ")
        if answer == "no" and number % 2 != 0 or answer == "yes" and number % 2 == 0:
            print("Correct!")
            k += 1
        else:
            if number % 2 != 0:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            elif number % 2 == 0:
                print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
    if k == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
