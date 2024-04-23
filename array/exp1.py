n=int(input("enter the size of the array"))
array = []
print("enter the elements")
for i in range (n):
    element=input("enter the element{}: ".format(i+1))
    array.append(element)
print("array is:",array)