def first_non_repeating(arr):
    counts = {}
    for i in arr:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    for i in arr:
        if counts[i] ==  1:
            return i
    return None
arr = [1, 2, 3, 2, 1, 4]
print(first_non_repeating(arr))
 