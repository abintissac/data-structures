n=int(input("enter the size of the array"))
array = []
for i in range (n):
    element=input("enter the element {}: ".format(i+1))
    array.append(element)
print(array)
new=input("enter new element to add")
array.append(new)
print("new array",array)
position_del=int(input("enter the position to delete"))
if position_del > 0 and position_del <= len(array):
    array.pop(position_del-1)
    print(array)
else:
    print("wrong position")
position_add=int(input("enter a position to add"))
if position_add > 0 and position_add <= len(array):
    new_element=input("enter new element")
    array.insert(position_add-1,new_element)
    print(array)
