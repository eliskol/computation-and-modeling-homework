from code import newton_rhapson, merge

assert merge([1, 2, 3], [-1, 2, 3]) == [-1, 1, 2, 2, 3, 3]
assert merge([1, 1, 1, 1], [1, 1, 1]) == [1, 1, 1, 1, 1, 1, 1]

assert newton_rhapson(2, 2, 0.001)**2 - 2 < 0.001
assert newton_rhapson(6, 5, 0.0001)**5 - 6 < 0.0001


