def newton_rhapson(x, n, precision):
    x_old = 1
    for i in range(0, 10):
        f = lambda p: (p**2) - x
        f_prime = lambda p : n * (p ** (n - 1))
        print((-1) / 2)
        x_new = x_old - f(x_old)/f_prime(x_old)
        # print(x_new)
        x_old = x_new
    return x_new


print(-1/2)

# print(newton_rhapson(2, 2, 50))


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

print(merge([1, 2, 3], [3, 5, 7, 8]))