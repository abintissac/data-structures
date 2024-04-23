def non_repeat_elements(my_list):
    freq_dict = {}
    for item in my_list:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1
    non_repeats = []
    for key in freq_dict:
        if freq_dict[key] == 1:
            non_repeats.append(key)

    return non_repeats
my_list = [1, 2, 3, 4, 5, 1, 2, 3, 6, 7, 8, 9, 7, 8, 9, 10]
print(non_repeat_elements(my_list))
