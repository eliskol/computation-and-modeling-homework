def sum_of_first_n_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def check_for_symmetry(input_string):
    if input_string == "":
        return True
    return input_string == input_string[::-1]


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

        else:
            return True
