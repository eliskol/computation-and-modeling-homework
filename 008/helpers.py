def merge(a, b):
    a_index = 0
    b_index = 0
    
    merged_list = []

    while len(merged_list) < (len(a) + len(b)):

        if a_index == len(a):
            for i in range(b_index, len(b)):
                merged_list.append(b[i])
        
        elif b_index == len(b):
            for i in range(a_index, len(a)):
                merged_list.append(a[i])

        elif a[a_index] < b[b_index]:
            merged_list.append(a[a_index])
            a_index += 1

        else:
            merged_list.append(b[b_index])
            b_index += 1

    return merged_list


def split_list(input_list):

    first_half_list = []
    second_half_list = []

    for i in range(0, len(input_list)):
        if i < int(len(input_list)/2):
            first_half_list.append(input_list[i])
        else:
            second_half_list.append(input_list[i])

    return first_half_list, second_half_list
