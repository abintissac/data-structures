def non_repeat(arr):
    counts = {}
    for i in arr:
        if i in counts:
            counts[i] += 1
        else:
            counts[i]=1
    list1 = []
    for key in counts:
        if counts[key]==1:
            list1.append(key)
    return list1
arr = [1,2,3,2,5,7,5,6,8,9]
print(non_repeat(arr))