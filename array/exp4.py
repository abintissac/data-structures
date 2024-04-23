n = int(input("Enter the size of the array: "))
array = []
for i in range(n):
    element = input("Enter element {}: ".format(i+1))
    array.append(element)
print("The array is:", array)
print("The length of the array is:", len(array))
new_element = input("Enter an element to add: ")
array.append(new_element)
print("Updated array:",array)
position_to_delete = int(input("Enter the position to delete: "))
if position_to_delete > 0 and position_to_delete <= len(array):
    array.pop(position_to_delete-1)
    print("Updated array:", array)
else:
    print("Invalid position entered.")
position_to_add = int(input("Enter the position to add: "))
if position_to_add > 0 and position_to_add <= len(array):
    new_element = input("Enter the value to add: ")
    array.insert(position_to_add-1, new_element)
    print("Updated array:", array)
else:
    print("Invalid position entered.")
array.sort()
print("Sorted array:", array)
array.reverse()
print("reversed array",array)

