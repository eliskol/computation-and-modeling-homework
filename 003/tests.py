from code import swap_sort
from code import tally_sort
from code import card_sort

assert swap_sort([-999, -0, 2367765, 0, -1, -1]) == [-999, -1, -1, 0, 0, 2367765]
assert swap_sort([-90, -99, -1, -1, 0, 3*8]) == [-99, -90, -1, -1, 0, 24]

assert tally_sort([-999, -0, 2367765, 0, -1, -1]) == [-999, -1, -1, 0, 0, 2367765]
assert tally_sort([-90, -99, -1, -1, 0, 3*8]) == [-99, -90, -1, -1, 0, 24]

assert card_sort([-999, -0, 2367765, 0, -1, -1]) == [-999, -1, -1, 0, 0, 2367765]
assert card_sort([-90, -99, -1, -1, 0, 3*8]) == [-99, -90, -1, -1, 0, 24]
