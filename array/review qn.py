from collections import Counter


def first_non_repeating_element(arr):
    count = Counter(arr)
    for elem in arr:
        if count[elem] == 1:
            return elem
    return None
arr = [1, 2, 3, 2, 1, 4]
print(first_non_repeating_element(arr))
