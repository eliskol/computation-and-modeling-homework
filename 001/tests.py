from code import check_for_symmetry
from code import sum_of_first_n_numbers
from code import convert_to_numbers, convert_to_letters


# check_for_symmetry tests
if check_for_symmetry('racecar') is not True:
    print('check_for_symmetry failed on input "racecar"')

if check_for_symmetry('batman') is not False:
    print('check_for_symmetry failed on input "batman"')

if check_for_symmetry('') is not True:
    print('check_for_symmetry failed on input ""')

if check_for_symmetry('!ab123 4 321ba!') is not True:
    print('check_for_symmetry failed on input "!ab123 4 321ba!"')

# sum_of_first_n_numbers tests
if sum_of_first_n_numbers(5) != 15:
    print('sum_of_first_n_numbers failed on input 5')

if sum_of_first_n_numbers(20) != 210:
    print('sum_of_first_n_numbers failed on input 20')

if sum_of_first_n_numbers(0) != 0:
    print('sum_of_first_n_numbers failed on input 20')

# convert_to_numbers tests
if convert_to_numbers('a cat') != [1, 0, 3, 1, 20]:
    print('convert_to_numbers failed on input "a cat"')

if convert_to_numbers('abcd') != [1, 2, 3, 4]:
    print('convert_to_numbers failed on input "abcd"')

if convert_to_numbers('a b c aa') != [1, 0, 2, 0, 3, 0, 1, 1]:
    print('convert_to_numbers failed on input "a b c aa"')

# convert_to_letters tests
if convert_to_letters([1, 2, 3, 4, 5]) != "abcde":
    print('convert_to_letters failed on input "[1, 2, 3, 4, 5]"')

if convert_to_letters([0, 1, 2, 27]) != " abA":
    print('convert_to_letters failed on input "[0, 1, 2, 27]"')
