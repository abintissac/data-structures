# text = "akhil jose"
# # print(len(text))
# #print(text.strip())
# # print(text.lower())
# # print(text.upper())
# # print(text.replace("l","k"))
#
# #print(text[5])
# for i in range(text[9]):
#     if i%2==0:
#         print(text.upper())
#     else:
#         print(text.lower())
#
# Take input string from user
str = input("Enter a string: ")
is_upper = True
for char in str:
    if is_upper:
        print(char.upper(), end="")
    else:
        print(char.lower(), end="")
    is_upper = not is_upper
print()
