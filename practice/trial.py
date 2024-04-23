def first_non_repeating(arr):
    counts = {}
    list1 =[]
    for i in arr:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    for i in arr:
        if counts[i] == 1:
            list1.append(i)
    return list1


arr = [1, 2, 3, 2, 1, 4]
print(first_non_repeating(arr))
