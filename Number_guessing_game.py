#!/usr/bin/env python3

# Created by: Nicholas Graziano
# Created on: November 2020
# This program checks if u got the right random number

import random

random_number = random.randint(1, 8)


def main():
    # this program checks if the random numbers match

    # input
    user_number_string = input("enter a number from 1, 8:")

    # process
    random_number == random.randint(1, 8)
    try:
        user_number = int(user_number_string)
        if user_number == random_number:
            print("You guessed correctly")
        else:
            print("you guessed incorrectly")
    except Exception:
        print("Not a number")


if __name__ == "__main__":
    main()
