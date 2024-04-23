def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n-1)) == 0
n = 12
if is_power_of_two(n):
    print("True")
else:
    print("False")
