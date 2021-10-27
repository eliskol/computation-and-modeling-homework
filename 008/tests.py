from code import merge_sort

example_list_1 = [-99, 13, 7564, 87, -876, 55]
example_list_2 = [-99, -100, 99, 100, 55, -55, 1, 22, 0, 0]

assert merge_sort(example_list_1) == [-876, -99, 13, 55, 87, 7564]
assert merge_sort(example_list_2) == [-100, -99, -55, 0, 0, 1, 22, 55, 99, 100]