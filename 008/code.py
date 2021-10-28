from helpers import *


def merge_sort(input_list):
    
    if len(input_list) > 1:

        middle_index = len(input_list) // 2

        first_half, second_half = input_list[:middle_index], input_list[middle_index:]

        sorted_first_half = merge_sort(first_half)
        sorted_second_half = merge_sort(second_half)
        
        return merge(sorted_first_half, sorted_second_half)
    
    else:
        return input_list
