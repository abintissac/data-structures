# Get input from user
arr = input("Enter the array elements separated by space: ").split()
freq = {}
for element in arr:
    if element in freq:
        freq[element] += 1
    else:
        freq[element] = 1
non_repeating = None
for element in arr:
    if freq[element] == 1:
        non_repeating = element
        break
if non_repeating:
    print(f"The first non-repeating element is {non_repeating}.")
else:
    print("There is no non-repeating element in the array.")
