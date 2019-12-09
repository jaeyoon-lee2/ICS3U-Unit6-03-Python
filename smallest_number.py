#!/user/bin/env python3

# Created by: Jaeyoon (Jay) Lee
# Created on: Dec 2019
# This program shows the smallest number in 10 random numbers

import random


def find_smallest_number(random_numbers):
    # this function find the smallest number in list

    smallest_number = 100

    for counter in random_numbers:
        if smallest_number > counter:
            smallest_number = counter

    return smallest_number


def main():
    # this function shows the smallest number in 10 random numbers

    random_numbers = []

    # input
    for loop_counter in range(0, 9):
        a_number = random.randint(1, 100)
        random_numbers.append(a_number)
        # print(a_number)

    # call the funciton
    smallest_number = find_smallest_number(random_numbers)

    # output
    print("The smallest number is: {0} ".format(smallest_number))


if __name__ == "__main__":
    main()
