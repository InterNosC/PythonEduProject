# Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).The numbers
# obtained should be printed in a comma-separated sequence on a single line.

def find_special_num():
    nums = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            nums.append(i)
    return nums


print(find_special_num(), end=',')

print((i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0), sep=",")
