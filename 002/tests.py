from code import encode, decode
from code import calc_square_root, calc_nth_root
from code import Stack, Queue
from code import calc_minimum, simple_sort

assert encode("bruh", 1, 1) == [3, 19, 22, 9], "encode failed"
assert encode("bruh", 3, 6) == [12, 60, 69, 30], "encode failed"

assert decode([12, 60, 69, 30], 3, 5) == "bruh", "decode failed"
assert decode([3, 19, 22, 9], 1, 1) == "bruh", "decode failed"

assert abs(calc_square_root(2, 0.00001) ** 2 - 2) < 0.0001, "square root failed"
assert abs(calc_square_root(3, 0.001) ** 2 - 3) < 0.01, abs(calc_square_root(3, 0.001) ** 2 - 3)

stack_test_1 = Stack()
stack_test_1.push("first item")
stack_test_1.push("next item")
stack_test_1.print()
print(stack_test_1.pop())

stack_test_2 = Stack([1, 2, 3])
stack_test_2.push(4)
stack_test_2.print()
print(stack_test_2.pop())

queue_test_1 = Queue()
queue_test_1.enqueue("first in queue")
queue_test_1.enqueue("second in queue")
queue_test_1.print()
print(queue_test_1.dequeue())

assert calc_minimum([-1, 2, 5, -7]) == -7, "calc_minimum failed"
assert calc_minimum([0, 123, 7465, -100]) == -100, "calc_minimum failed"

assert simple_sort([5, 4, 3, 6, 1]) == [1, 3, 4, 5, 6], "simple_sort failed"
assert simple_sort([5, 4, 3, 6, 1, -129387]) == [-129387, 1, 3, 4, 5, 6], "simple_sort failed"