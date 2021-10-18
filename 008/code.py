from helpers import merge

def split_list(input_list):

    first_half_list = []
    second_half_list = []

    for i in range(0, len(input_list)):
        if i < int(len(input_list)/2):
            first_half_list.append(input_list[i])
        else:
            second_half_list.append(input_list[i])
    
    return first_half_list, second_half_list

ex_list = [5, 2, 3, 4, 5]
# print(split_list(ex_list))

def merge_sort(input_list):
    
    if len(input_list) > 1:
        first_half, second_half = split_list(input_list)

        sorted_first_half = merge_sort(first_half)
        sorted_second_half = merge_sort(second_half)
        
        return merge(sorted_first_half, sorted_second_half)
    
    else:
        return input_list

print(merge_sort(ex_list))