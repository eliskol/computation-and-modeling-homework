def calc_minimum(numbers):

    min_num = numbers[0]

    for number in numbers:

        if number < min_num:

            min_num = number

    return min_num


def calc_maximum(numbers):

    max_num = numbers[0]

    for number in numbers:

        if number > max_num:

            max_num = number

    return max_num


def shift_left(list, index_to_move):
    list.insert(index_to_move - 1, list.pop(index_to_move))
    return list 
