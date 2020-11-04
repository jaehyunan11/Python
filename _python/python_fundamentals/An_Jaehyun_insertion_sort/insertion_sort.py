def insertion_sort(my_list):
    for idx in range(1, len(my_list)):
        current = my_list[idx]
        prev_idx = idx - 1
        while my_list[prev_idx] > current and prev_idx >= 0:
            my_list[prev_idx+1] = my_list[prev_idx]
            prev_idx -= 1
        my_list[prev_idx+1] = current
        print(my_list)
    return my_list

sample_list = [23,73,17,86,34,8]
print(sample_list)
print(insertion_sort(sample_list))

