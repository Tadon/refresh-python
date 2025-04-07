'''
Prompt:
You are given a list of numbers from 1 to n, but one number is missing.
Write a function find_missing_number(nums) that returns the missing number.

Assume:

    The list has no duplicates.

    Only one number is missing.

Examples:

find_missing_number([1, 2, 4, 5, 6]) → 3
find_missing_number([3, 7, 1, 2, 8, 4, 5]) → 6
find_missing_number([1, 2, 3, 5]) → 4
'''

def find_missing_number(nums):
    integer = sorted(nums)[0]
    if integer != 1:
        return 1
    for num in sorted(nums):
        if num == integer:
            integer += 1
        else:
            return integer
    return integer
    

print(find_missing_number([1, 2, 4, 5, 6]))        # 3
print(find_missing_number([3, 7, 1, 2, 8, 4, 5]))  # 6
print(find_missing_number([1, 2, 3, 5]))            # 4
print(find_missing_number([1, 3]))                  # 2
print(find_missing_number([1, 2, 4, 5, 6]))         # 3
print(find_missing_number([1, 2, 3, 4, 6, 7, 8]))   # 5
print(find_missing_number([1, 3]))                  # 2
print(find_missing_number([1, 2, 3, 5]))            # 4
print(find_missing_number([1, 2, 3, 4, 5, 6, 8]))   # 7
print(find_missing_number([1, 2]))                  # 3
print(find_missing_number([1, 3, 4, 5]))            # 2
print(find_missing_number([1, 2, 4]))               # 3
print(find_missing_number([1, 2, 3, 5, 6]))         # 4
print(find_missing_number([1]))                     # 2