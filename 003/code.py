from help import calc_minimum, calc_maximum
from help import shift_left


def swap_sort(numbers):

    for i in range(0, len(numbers) - 1):

        for j in range(0, len(numbers) - 1):

            if numbers[j] > numbers[j+1]:

                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


def tally_sort(numbers):

    smallest_number = calc_minimum(numbers)

    shifted_numbers = []
    tallies = []
    sorted_list = []
    
    for i in range(0, len(numbers)):
        shifted_numbers.append(numbers[i] - smallest_number)

    for i in range(calc_maximum(shifted_numbers) + 1):
        tallies.append(0)

    for number in shifted_numbers:
        tallies[number] += 1

    for i, number in enumerate(tallies):
        for j in range(number):
            sorted_list.append(i + smallest_number)

    return sorted_list


def card_sort(numbers):

    for i in range(len(numbers)):
        mutable_index = i
        while numbers[mutable_index] < numbers[mutable_index - 1] and mutable_index > 0:
            numbers.insert(mutable_index - 1, numbers.pop(mutable_index))
            mutable_index -= 1

    return numbers
