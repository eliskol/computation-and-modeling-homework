import math


def sum_of_first_n_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def check_for_symmetry(input_string):
    if input_string == "":
        return True
    return input_string == input_string[:: - 1]


def convert_to_numbers(input_string):

    alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHILMNOPQRSTUVWYXZ"

    output_list = []

    for letter in input_string:
        output_list.append(alphabet.index(letter))

    return output_list


def convert_to_letters(input_list):

    alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHILMNOPQRSTUVWYXZ"

    output_string = ""

    for number in input_list:
        output_string += alphabet[number]

    return output_string


def is_prime(n):

    for i in range(2, (n//2)+1):

        if n % i == 0:
            return False

        elif i == (n//2):
            return True


def get_intersection(list1, list2):

    output_list = []

    for item in list1:

        if item in list2:

            if item not in output_list:

                output_list.append(item)

    return output_list


def get_union(list1, list2):
    output_list = []

    for item in list1:
        if item not in output_list:
            output_list.append(item)

    for item in list2:
        if item not in list1:
            output_list.append(item)

    return output_list


def count_characters(input_string):

    output_dict = {}

    lowercase_input_string = input_string.lower()

    for character in lowercase_input_string:
        output_dict[character] = lowercase_input_string.count(character)

    return output_dict


def get_first_n_terms_nonrecursive(n):

    term_list = []

    for i in range(1, n+1):

        if i == 1:
            new_term = 5
            term_list.append(new_term)

        else:
            new_term = 3 * (term_list[i-2]) - 4
            term_list.append(new_term)

    return term_list


def get_nth_term_recursive(n):

    if n == 1:
        return 5

    else:
        return 3 * get_nth_term_recursive(n-1) - 4


def convert_to_base_10(input_binary):

    input_binary_string = str(input_binary)

    reversed_binary_string = input_binary_string[::-1]

    output = 0

    for index, number in enumerate(reversed_binary_string):

        if int(number) == 1 or int(number) == 0:

            output += int(number) * 2**index

        else:
            return("input is not binary!")

    return(output)


def convert_to_base_2(n):

    exponent_list = []

    output = 0

    while n > 0:

        n_log_base_2 = math.log(n, 2)
        rounded_log = math.floor(n_log_base_2)

        n = n - 2**rounded_log

        exponent_list.append(rounded_log)

    for exponent in exponent_list:
        output += 10**exponent

    return(output)
