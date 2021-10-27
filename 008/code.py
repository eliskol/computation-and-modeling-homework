from helpers import *


def merge_sort(input_list):
    
    if len(input_list) > 1:
        first_half, second_half = split_list(input_list)

        sorted_first_half = merge_sort(first_half)
        sorted_second_half = merge_sort(second_half)
        
        return merge(sorted_first_half, sorted_second_half)
    
    else:
        return input_list
