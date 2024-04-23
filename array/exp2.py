n=int(input("enter the size of the array"))
array = []
for i in range (n):
    element=input("enter the elements {}: ".format(i+1))
    array.append(element)
print("array is : ",array)
print(len(array))
add=input("enter an element to add ")
array.append(add)
print(array)