from code import check_for_symmetry
from code import sum_of_first_n_numbers
from code import convert_to_numbers, convert_to_letters
from code import is_prime
from code import get_intersection, get_union
from code import count_characters
from code import get_first_n_terms_nonrecursive, get_nth_term_recursive
from code import convert_to_base_10, convert_to_base_2

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

# is_prime tests
if is_prime(10) is not False:
    print('is_prime failed on input 10')

if is_prime(11) is not True:
    print('is_prime failed on input 11')
    print(is_prime(11))

# get_intersection tests
if get_intersection([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 6, 7, 8]) != [1, 2, 3, 4]:
    print('get_intersection failed')
    print(get_intersection([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 6, 7, 8]))

if get_intersection([1, 1, 1, 1, 1], []) != []:
    print('get_intersection failed on input "[1, 1, 1, 1, 1], []"')
    print(get_intersection([1, 1, 1, 1, 1], []))

# get_union tests

if get_union([1, 2, 3, 4, 5, 5, 5, 5], [1, 5, 7, 8]) != [1, 2, 3, 4, 5, 7, 8]:
    print('get_union is a failure')
    print(get_union([1, 2, 3, 4, 5, 5, 5, 5], [1, 5, 7, 8]))

if get_union(['a', 'b', 1, 2, 3], [1, 4, 5, 6, 'b']) != ['a', 'b', 1, 2, 3, 4, 5, 6]:
    print('get_union is a failure')
    print(get_union(['a', 'b', 1, 2, 3], [1, 4, 5, 6, 'b']))

# count_characters tests

test1 = dict({'a': 1, 'b': 1, 'c': 1})

assert count_characters('abc') == test1

test2 = dict({' ': 1, '!': 1, 'a': 2})

assert count_characters('a a!') == test2

# get_first_n_terms_nonrecursive tests

nonrecursive_test1 = [5, 11, 29]

assert get_first_n_terms_nonrecursive(3) == nonrecursive_test1

nonrecursive_test2 = [5, 11, 29, 83]

assert get_first_n_terms_nonrecursive(4) == nonrecursive_test2

# get_nth_term_recursive tests

get_nth_term_recursive_test1 = 83

assert get_nth_term_recursive(4) == get_nth_term_recursive_test1

get_nth_term_recursive_test2 = 245

assert get_nth_term_recursive(5) == get_nth_term_recursive_test2

# convert_to_base_10 tests

convert_to_base_10_test1 = 7

assert convert_to_base_10(111) == convert_to_base_10_test1

convert_to_base_10_test2 = 11

assert convert_to_base_10(1011) == convert_to_base_10_test2

# convert_to_base_2 tests

assert convert_to_base_2(10) == 1010

assert convert_to_base_2(20) == 10100
