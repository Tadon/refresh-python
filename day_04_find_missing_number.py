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

''' Initial version
def find_missing_number(nums):
    integer = sorted(nums)[0]               #setting counter to beginning of array
    if integer != 1:                        #if beginning of array isn't 1, we know the missing number is 1 - return it
        return 1            
    for num in sorted(nums):                #iterating through array
        if num == integer:                  #checking to see if the current position integer in the array is the same number as the counter (named integer)
            integer += 1                    #iterating the counter to the next position in the array
        else:
            return integer                  #if the counter does not match the current integer in the array, we know that this is the missing number, and we return the counter
    return integer                          #if we have iterated through the entire sorted array without finding a mis matched number, we know the number that is missing is the number that should be at the end of the array (+1 from the current end number)
'''    

#Faster version
def find_missing_number(nums):              #uses mathmatical formula to do the same thing with less steps
    n = len(nums) + 1                       #this is how long the array nums is supposed to be (remember only 1 number is ever missing, so we have to assume that the correct length of the array is length of the array + 1)
    correct_sum = (n * (n + 1)) // 2         #this is a math formula to find the sum of all numbers in an array that starts at 1 and ends at n
    return correct_sum - sum(nums)           #returning the difference between what the total sum should be, and what the total sum is. This returns our missing number


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