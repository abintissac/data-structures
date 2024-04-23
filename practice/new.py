# def comp(a):
#     for i in a:
#         if a[i]>a[i+1]:
#             max=a[i]
#         else:
#             a[i]=a[i+1]
#     return max
# a=[1,2,3,4,8,2]
# print(comp(a))
a=[1,2,3,4,5]

print(max(a))
b=max(a)
for i in range(5):
    a[i]+=1
print(a)
for i in range(5):
    if a[i]<b:
        print("true")
    else:
        print("false")







