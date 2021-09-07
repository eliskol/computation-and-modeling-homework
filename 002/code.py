import random


def encode(string, a, b):

    alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHILMNOPQRSTUVWYXZ"

    output_list = []

    for letter in string:

        trivial_encoded_letter = alphabet.index(letter)

        if a != 0:

            linear_encoded_letter = a * trivial_encoded_letter + b

        else:   
            linear_encoded_letter = trivial_encoded_letter + b

        output_list.append(linear_encoded_letter)

    return output_list


def decode(input_list, a, b):

    alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHILMNOPQRSTUVWYXZ"

    output_string = ""

    for number in input_list:

        if a != 0:

            output_string += alphabet[int((number - b) / a)]

        else:

            output_string += alphabet[(number - b)]

    return output_string


def bisection_search(n, a, b, precision):

    while (b - a) > precision:

        # 0.000000000000001 is most precise possible

        guess = (a + b) / 2

        if guess**2 == n:

            return guess

        elif guess**2 < n:
            a = (a + b) / 2

        elif guess**2 > n:
            b = (a + b) / 2
    return guess


def calc_square_root(x, precision):

    a = 0

    b = x + 1

    while (b - a) > precision:

        guess = (a + b) / 2

        if guess**2 == x:

            return guess

        elif guess**2 < x:
            a = (a + b) / 2

        elif guess**2 > x:
            b = (a + b) / 2
    return guess


def calc_nth_root(x, n, precision):

    a = 0

    b = x + 1

    while (b - a) > precision:

        guess = (a + b) / 2

        if guess**n == x:

            return guess

        elif guess**n < x:
            a = (a + b) / 2

        elif guess**n > x:
            b = (a + b) / 2

    return guess


class Stack:

    def __init__(self, contents=None):

        if contents is None:
            self.contents = []

        else:
            self.contents = contents

    def print(self):

        for item in self.contents[::-1]:

            print(item)

    def push(self, item_to_push):

        self.contents.append(item_to_push)

    def pop(self):
        return self.contents.pop()


class Queue:

    def __init__(self, contents=None):

        if contents is None:
            self.contents = []

        else:
            self.contents = contents

    def print(self):

        for item in self.contents:

            print(item)

    def enqueue(self, item_to_queue):

        self.contents.append(item_to_queue)

    def dequeue(self):

        return self.contents.pop(0)


def calc_minimum(numbers):

    min_num = numbers[0]

    for number in numbers:

        if number < min_num:

            min_num = number

    return min_num


def simple_sort(numbers):

    output_list = []

    for number in numbers.copy():

        next_lowest = calc_minimum(numbers)

        output_list.append(next_lowest)

        numbers.remove(next_lowest)

    return output_list
